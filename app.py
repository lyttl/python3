#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template, abort
import os,json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    filepath = '/home/shiyanlou/files'
    files = os.listdir(filepath)
    file_list = []
    for filess in files:
        filename = os.path.join(filepath,filess)
        with open(filename,'r') as file:
            new_file = json.loads(file.read())
            file_list.append(new_file)
    return render_template('index.html',file_list=file_list)

@app.route('/files/<filename>')
def file(filename):
    real_file = "{}.json".format(filename)
    filepath  = '/home/shiyanlou/files'
    file_join = os.path.join(filepath,real_file)
    file_exist = os.path.exists(file_join)
    if file_exist:
        with open(file_join,'r') as file:
            new_file = json.loads(file.read())
        return render_template('file.html',new_file=new_file)
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
