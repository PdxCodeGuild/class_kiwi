from flask import Flask, render_template, request

app = Flask(__name__)


# localhost:5000/


@app.route('/')
def index():
    name = "Ryan"
    return render_template('index.html', name=name)


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
