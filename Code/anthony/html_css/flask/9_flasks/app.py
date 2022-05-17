
from flask import Flask, render_template


app = Flask(__name__)

# localhost:5000/


@app.route('/')
def index():
    name = "Bill"
    return render_template('index.html', name=name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contact():
    return render_template('contact.html')


@app.route('/check-grade/<int:grade>')
def check_grade(grade):
    return render_template('check-grade.html', grade=grade)
