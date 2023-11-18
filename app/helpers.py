def read_templates(tag, tag_data):
    tag_template_text = f"{{% macro {tag}(e) %}}\n"
    for i in tag_data.get('include'):
        tag_template_text += "{{ " + f"parts['{i}'](e)" + " }}\n"
    tag_template_text += "{% endmacro %}"
    print(tag_template_text)
    return tag_template_text
