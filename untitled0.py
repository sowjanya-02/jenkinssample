#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:52:37 2021

@author: sowjanyagunturu
"""

from flask import Flask, render_template

import socket


app = Flask(__name__)

@app.route('/')
def home():
   hostname = socket.gethostname()
   return 'welcome to jenkins example :)'.format(hostname)
