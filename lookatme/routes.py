from typing import Union

from flask import current_app, g, render_template

from .helpers import get_sort_date


def home() -> str:
    return render_template("base/about.html", tag="about")


def page(tag: str) -> Union[str, bytes]:
    if tag == "hello":
        return b"Hello world!!!!"
    else:
        if tag not in g.tag_templates:
            current_app.logger.debug(g.tag_templates)
            current_app.logger.debug(f"looking for {tag}...")
            try:
                tag = next(
                    k for k, v in g.tag_templates.items() if v.get("endpoint") == tag
                )
                current_app.logger.debug(f"using {tag} as tag...")
            except StopIteration:
                current_app.logger.debug("no alt endpoint found!")
                return render_template("base/about.html", tag="about")

        filtered_entries = sorted(
            [e for e in g.entries if tag in e["tags"]],
            key=lambda e: get_sort_date(e),
            reverse=True,
        )
        parts_list = g.tag_templates.get(tag).get("parts")
        sep = g.tag_templates.get(tag).get("sep")
        header_text = g.tag_templates.get(tag).get("header-text", tag)
        return render_template(
            "base/page.html",
            parts_list=parts_list,
            header_text=header_text,
            entries=filtered_entries,
            sep=sep,
        )
