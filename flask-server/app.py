#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:06:41 2019

@author: joseph
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

UPLOAD_FOLDER = "./files"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
