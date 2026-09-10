"""Build Jekyll and check generated pages using only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
import os
import subprocess
import sys
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
# Exercise repository-subpath links just like GitHub Pages.
BASE = "/Oman-guide"


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.tables = []
        self.row = None
        self.errors = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "img" and "alt" not in attrs:
            self.errors.append("Image is missing alt text")
        if tag == "table":
            self.tables.append([])
        if tag == "tr":
            self.row = 0
        if tag in ("td", "th") and self.row is not None:
            self.row += int(attrs.get("colspan", "1"))

    def handle_endtag(self, tag):
        if tag == "tr" and self.tables and self.row is not None:
            self.tables[-1].append(self.row)
            self.row = None


def review(output, base):
    pages = {p.resolve(): Page(p.read_text(encoding="utf-8"))
             for p in output.rglob("*.html")}
    errors = []
    if not pages:
        return ["No HTML pages were generated"]
    for path, page in pages.items():
        label = path.relative_to(output)
        errors.extend(f"{label}: {error}" for error in page.errors)
        for rows in page.tables:
            if len(set(rows)) > 1:
                errors.append(f"{label}: inconsistent table column counts: {rows}")
        current = f"{base}/{label.as_posix()}"
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = urlsplit(urljoin(current, link))
            target_path = unquote(target.path)
            if not target_path.startswith(base + "/"):
                errors.append(f"{label}: link escapes repository base path: {link}")
                continue
            local = (output / target_path[len(base) + 1:]).resolve()
            if not local.is_relative_to(output):
                errors.append(f"{label}: link escapes output folder: {link}")
                continue
            if local.is_dir():
                local /= "index.html"
            if not local.is_file():
                errors.append(f"{label}: missing link/image target: {link}")
            elif target.fragment and local in pages:
                if unquote(target.fragment) not in pages[local].ids:
                    errors.append(f"{label}: missing anchor: {link}")
    print(f"Reviewed {len(pages)} HTML pages.", flush=True)
    return errors


def main():
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    subprocess.run(["git", "diff", "--cached", "--check"], cwd=ROOT, check=True)
    env = dict(os.environ, JEKYLL_ENV="production")
    subprocess.run(
        ["ruby", "-S", "bundle", "exec", "jekyll", "build", "--strict_front_matter",
         "--destination", str(OUTPUT), "--baseurl", BASE],
        cwd=ROOT / "docs", env=env, check=True,
    )
    errors = review(OUTPUT.resolve(), BASE)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Site checks passed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (subprocess.CalledProcessError, OSError) as error:
        print(f"Site check failed: {error}", file=sys.stderr)
        sys.exit(1)
