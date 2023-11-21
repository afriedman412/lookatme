from flask import g, render_template

from .helpers import get_sort_date


def home() -> str:
    return render_template("base/about.html", tag="about")


def page(tag: str) -> str:
    if tag not in g.tag_templates:
        try:
            tag = next(
                k for k, v in g.tag_templates.items() if v.get("endpoint") is tag
            )
        except StopIteration:
            pass
    else:
        filtered_entries = sorted(
            [e for e in g.entries if tag in e["tags"]],
            key=lambda e: get_sort_date(e),
            reverse=True,
        )
        if tag in g.tag_templates:
            parts_list = g.tag_templates.get(tag).get("parts")
            header_text = tag
            if "header-text" in g.tag_templates.get(tag):
                header_text = g.tag_templates.get(tag)["header-text"]
            return render_template(
                "base/page.html",
                parts_list=parts_list,
                header_text=header_text,
                entries=filtered_entries,
            )
    return render_template("base/about.html", tag="about")
