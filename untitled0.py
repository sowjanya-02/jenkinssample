#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:52:37 2021

@author: sowjanyagunturu
"""

from flask import Flask, render_template

import socket


app = Flask(__name__)
#app = create_app()
#@app.route('/')
#def hello():
   #hostname = socket.gethostname()
   #return 'welcome to conn! store microservice is running on {} pod :)'.format(hostname)
@app.route('/')
def home():
   hostname = socket.gethostname()
   return 'welcome to jenkins example :)'.format(hostname)