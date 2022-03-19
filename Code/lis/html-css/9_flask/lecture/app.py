# https://github.com/PdxCodeGuild/class_kiwi/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/12%20Flask.md
from flask import Flask, render_template, result


app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
    name = "Astro"
    return render_template('index.html', name=name, animal='Awesome Kosmo!')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/check-grade/<int:grade>')
def check_grade(grade):
    return render_template('check-grade.html', grade=grade)


@app.route('/llama', methods=['POST'])
def display_name():
    name = request.form['panda']
    return render_template('contact.html', name=name)
