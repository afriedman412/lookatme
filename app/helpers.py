from jinja2 import Environment, select_autoescape


def read_templates(tag, tag_data):
    tag_template_text = f"{{% macro {tag}(e) %}}\n"
    for i in tag_data.get('include'):
        tag_template_text += "{{ " + f"parts['{i}'](e)" + " }}\n"
    tag_template_text += "{% endmacro %}"
    print(tag_template_text)
    return tag_template_text


def render_macro(tag_template_text):
    template = Environment(
        autoescape=select_autoescape(
            ['html', 'xml']
            )).from_string(tag_template_text)
    return template.render()
