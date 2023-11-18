from flask import render_template, g
from datetime import datetime as dt


def get_sort_date(entry):
    if 'work' in entry['tags'] and 'end_date' not in entry:
        return dt.now()
    else:
        return dt.strptime(entry['date'], "%m-%d-%Y")


def home():
    return render_template('base/about.html', tag='about', entries=g.entries)


def page(tag):
    filtered_entries = sorted(
      [e for e in g.entries if tag in e['tags']],
      key=lambda e: get_sort_date(e), reverse=True
      )
    if tag in g.tag_templates:
        parts_list = g.tag_templates.get(tag).get('parts')
        header_text = tag
        if "header-text" in g.tag_templates.get(tag):
            header_text = g.tag_templates.get(tag)['header-text']
        return render_template(
            'base/page.html',
            parts_list=parts_list,
            header_text=header_text,
            entries=filtered_entries)
    else:
        return render_template(
            'base/about.html',
            tag='about',
            entries=g.entries)
