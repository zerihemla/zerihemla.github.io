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

## Build

```bash
python build.py
```

This writes `docs/index.html` and copies `static/` into `docs/static/`.
Preview it locally:

```bash
./scripts/test_run.sh
```

Then open http://localhost:8000

