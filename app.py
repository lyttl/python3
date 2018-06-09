#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template
import os,json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    filepath = '/home/shiyanlou/files'
    files = os.listdir(filepath)
    for f in files:
        file_path = os.path.join(filepath,f)
        print(file_path)
        with open(file_path) as file:
           file_dict =  file.read()
           return file_dict
@app.route('/files/<filename>')
def file(filename):
    filename = '/home/shiyanlou/files/filename.json'
    tf = os.path.exists(filename)
    if tf:
        with open(filename,'r') as file:
            new_file = json.load(file.read())
    
    else:
        @app.errorhandler(404)
        def not_found(error):
            return render_template('shiyanlou 404'),404


