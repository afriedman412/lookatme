from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
   return render_template(f'page.html', tag='home')

@app.route('/<tag>')
def data(tag):
   with open('entries.json') as json_file:
      data = json.load(json_file)
   return render_template(f'page.html', data=data, tag=tag)

if __name__=="__main__":
   app.run()