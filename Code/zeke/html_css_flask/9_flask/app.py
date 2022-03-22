from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/about')
def about():
    return 'this is the about page!'
