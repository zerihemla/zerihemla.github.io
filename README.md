# resume-site

A Python-generated resume/portfolio site. Content lives in `data.py`,
layout in `templates/index.html.j2`, styling in `static/css/style.css`.
`build.py` renders it all to `docs/index.html`, which GitHub Pages serves.

## Local setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Edit your content

Open `data.py` and fill in your real name, links, skills, projects,
and experience. No HTML editing needed for content changes.

## Build

```bash
python build.py
```

This writes `docs/index.html` and copies `static/` into `docs/static/`.
Preview it locally:

```bash
cd docs && python -m http.server
```

Then open http://localhost:8000

## Deploy

Push to GitHub with Pages configured to serve from the `docs/` folder
on `main` (see repo setup steps). The included GitHub Actions workflow
(`.github/workflows/deploy.yml`) will also auto-rebuild `docs/` on every
push, so editing `data.py` and pushing is enough — you don't have to
run `build.py` and commit the output yourself.
