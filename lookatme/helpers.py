import logging
from datetime import datetime as dt
from logging.handlers import RotatingFileHandler
from typing import Any


def add_log() -> RotatingFileHandler:
    log_file_path = "app.log"
    file_handler = RotatingFileHandler(log_file_path, maxBytes=10240, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
    return file_handler


def get_sort_date(entry: dict[str, Any]) -> dt:
    if not entry.get("date"):
        return dt.now()
    elif "work" in entry["tags"] and "end_date" not in entry:
        return dt.now()
    else:
        return dt.strptime(entry["date"], "%m-%d-%Y")


def read_templates(tag: str, tag_data: dict[str, Any]) -> str:
    tag_template_text = f"{{% macro {tag}(e) %}}\n"
    for i in tag_data.get("include", []):
        tag_template_text += "{{ " + f"parts['{i}'](e)" + " }}\n"
    tag_template_text += "{% endmacro %}"
    return tag_template_text


def create_header_links(tag_templates: dict[str, Any], connector: str = " • ") -> str:
    header_links = []
    for t in sorted(tag_templates, key=lambda t: tag_templates[t].get("priority", 999)):
        endpoint = tag_templates[t].get("endpoint", t).lower()
        link_text = tag_templates[t].get("header-text", t).title()
        header_links.append(f"<a href='/{endpoint}'>{link_text}</a>")
    return connector.join(header_links)
