from flask import render_template, url_for
import json
import os


def home():
   return render_template('page.html', tag='home')

def page(tag):
   with open("entries.json") as json_file:
      data = json.load(json_file)
   return render_template('page.html', data=data, tag=tag)