from flask import Flask, url_for, render_template
from flask import request, jsonify
from sys import argv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "<pre> go to /now to get the current time :D </pre>"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/<string:page_name>/')
def render_static(page_name):
    user = request.args.get('name')
    return render_template('%s.html' % page_name, **locals())

@app.route('/now')
def time_now():
    now = datetime.now()
    current_time = { "current_time": now.strftime("%H:%M:%S") }
    return jsonify(current_time)    
    #return "<pre> Current time: {} </pre>".format(current_time)

if __name__ == '__main__':
    app.run("0.0.0.0",argv[1])
