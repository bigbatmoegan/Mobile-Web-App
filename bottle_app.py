# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, post, get, template

import sqlite3
db=sqlite3.connect("./mysite/wings.db")
c=db.cursor()


@route('/')
def index():
    return template("main.html", c=c)

@post('/getWings')
def getWings():
    return template("getWings.html", c=c)

@post('/results2')
def results2():
    return template("results2.html", c=c)


application=default_app()