from datetime import datetime as dt
from typing import Any


def get_sort_date(entry: dict[str, Any]) -> dt:
    if "work" in entry["tags"] and "end_date" not in entry:
        return dt.now()
    else:
        return dt.strptime(entry["date"], "%m-%d-%Y")


def read_templates(tag: str, tag_data: dict[str, Any]) -> str:
    tag_template_text = f"{{% macro {tag}(e) %}}\n"
    for i in tag_data.get("include", []):
        tag_template_text += "{{ " + f"parts['{i}'](e)" + " }}\n"
    tag_template_text += "{% endmacro %}"
    print(tag_template_text)
    return tag_template_text
