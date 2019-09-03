#!/usr/bin/python3
""" 0. Script to start a Flask web application """

from flask import Flask

app = Flask(__name__)

from app import routes
