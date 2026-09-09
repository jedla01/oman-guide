# Omán 2027

A Czech-language travel guide, ready to populate for a trip to Oman in 2027.
The site uses Jekyll and the Cayman theme.

## Editing the guide

- `docs/index.md`: trip overview, preparation, transport, accommodation and budget.
- `docs/den1.md` and `docs/den2.md`: starter daily itineraries.
- `docs/_config.yml`: site title, description and language.
- `docs/assets/`: styles and any new trip images.

To add a day, copy a daily page and give it a unique title, permalink and
`nav_order`. Pages with `nav_order` appear in the header navigation automatically.
Use Jekyll's `relative_url` filter for internal links so they also work under a
GitHub Pages repository subpath.

## Local preview

Install Ruby and Bundler, then run from the repository root:

```sh
cd docs
bundle install
bundle exec jekyll serve
```

Open the local address printed by Jekyll. Restart the server after changing
`_config.yml`. The remote theme needs network access when building.

To build into the root output folder:

```sh
cd docs
bundle exec jekyll build --destination ../_site
```

Edit the source in `docs/`; `_site/` contains generated output and is ignored by Git.

## GitHub Pages

In the repository's **Settings → Pages**, select **GitHub Actions** as the build
source. The workflow in `.github/workflows/jekyll.yml` builds `docs/` and deploys
on pushes to `main`, or when run manually. It supplies the repository base path
automatically.

The starter deliberately leaves dates, reservations and travel details to fill in.