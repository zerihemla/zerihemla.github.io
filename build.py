"""
Renders templates/index.html.j2 -> docs/index.html and copies
static/ -> docs/static/. Run this after editing data.py, templates,
or CSS/JS. GitHub Pages is configured to serve from /docs.
"""

import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from data import RESUME

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUTPUT = ROOT / "docs"


def build():
    env = Environment(loader=FileSystemLoader(TEMPLATES))
    template = env.get_template("index.html.j2")
    html = template.render(resume=RESUME)

    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "index.html").write_text(html, encoding="utf-8")

    static_out = OUTPUT / "static"
    if static_out.exists():
        shutil.rmtree(static_out)
    shutil.copytree(STATIC, static_out)

    print(f"Built site -> {OUTPUT / 'index.html'}")


if __name__ == "__main__":
    build()
