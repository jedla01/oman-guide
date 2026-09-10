# Omán 2027

A Czech-language travel guide for 13–21 March 2027, with a provisional eight-day itinerary.
The site uses Jekyll and the Cayman theme.

## Editing the guide

- `docs/index.md`: trip overview, preparation, transport, accommodation and budget.
- `docs/lety.md`: selected flights, connections and fare comparison in euros.
- `docs/den1.md` through `docs/den8.md`: daily plans and items to verify.
- `docs/_config.yml`: site title, description and language.
- `docs/assets/`: styles and any new trip images.

The visual style uses Oman's red, white and green flag palette. The local flag image
comes from the [Oman Foreign Ministry downloads](https://www.fm.gov.om/en/ministry/media/downloads/).

To add a day, copy a daily page and give it a unique title, permalink and
`nav_order`. Pages with `nav_order` appear in the header navigation automatically.
Use Jekyll's `relative_url` filter for internal links so they also work under a
GitHub Pages repository subpath.

## Local preview

Install Ruby and Bundler, then run from the repository root:

```sh
cd docs
bundle install
bundle exec jekyll serve --livereload
```

Open the local address printed by Jekyll. Restart the server after changing
`_config.yml`. The remote theme needs network access when building.
Saved page and style changes rebuild automatically and refresh the browser.
Check both desktop and narrow mobile widths when changing the layout.

To build into the root output folder:

```sh
cd docs
bundle exec jekyll build --destination ../_site
```

Edit the source in `docs/`; `_site/` contains generated output and is ignored by Git.

## Automatic checks before pushing

With Ruby, Bundler and Python 3.9+ on your PATH, run from the repository root:

```sh
python scripts/check-site.py
```

This builds the production site with a repository base path and checks generated
HTML for broken internal links, missing images, missing anchors, missing image
alt attributes and inconsistent table column counts. It also checks staged and
unstaged changes for whitespace errors. External websites, CSS image URLs and
visual appearance are not checked; use the browser preview for layout review.

Enable the automatic pre-push check once per clone:

```sh
git config core.hooksPath .githooks
```

A failed check blocks `git push`. The hook checks the current working tree, so
commit the changes you reviewed before pushing. It requires network access to
download the remote theme. Git clients must have Ruby and Python on their PATH.
If you already use custom hooks, merge this pre-push command into them instead
of replacing your hooks path. To disable this hook configuration:

```sh
git config --unset core.hooksPath
```

## GitHub Pages

In the repository's **Settings → Pages**, select **GitHub Actions** as the build
source. The workflow in `.github/workflows/jekyll.yml` builds `docs/` and deploys
on pushes to `main`, or when run manually. It supplies the repository base path
automatically.

The itinerary is a draft; flight times, bookings, travel times and visiting conditions remain to be confirmed.
