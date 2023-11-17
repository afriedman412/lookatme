from flask import render_template, g
from datetime import datetime as dt
import yaml
import os

def get_sort_date(entry):
   if 'work' in entry['tags'] and 'end_date' not in entry:
      return dt.now()
   else:
      return dt.strptime(entry['date'], "%m-%d-%Y")

def home():
   from .page_data import content
   return render_template('about.html', tag='about', entries=content)


def page(tag):
   from .page_data import entries
   filtered_entries = sorted(
      [e for e in entries if tag in e['tags']], 
      key=lambda e: get_sort_date(e), reverse=True
      )

   if tag in g.tag_templates:
      parts_list = g.tag_templates.get(tag).get('parts')
      return render_template(
         'page.html',
         parts_list=parts_list,
         header_text=tag,
         entries=filtered_entries)
   else:
      return "poop"
