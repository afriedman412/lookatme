from flask import render_template
import json


def home():
   return render_template(f'page.html', tag='home')

def page(tag):
   with open('./app/data/entries.json') as json_file:
      data = json.load(json_file)
   return render_template(f'page.html', data=data, tag=tag)