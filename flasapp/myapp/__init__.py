from flask import Flask, render_template, flash, redirect, url_for, session, request, logging


app= Flask(__name__)

app.config.from_pyfile('config.py')

from myapp import views
from myapp import models
from myapp import config