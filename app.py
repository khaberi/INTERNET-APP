from flask import flask

app = flask(__name__)


@app.route ("/about")
def hello ()
return "hello, world"
