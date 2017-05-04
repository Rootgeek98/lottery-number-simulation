from flask import render_template
from . import main

@main.route('/trend/')
def trend():
    return render_template('trend.html')

@main.route('/')
def index():
    return render_template('index.html')
