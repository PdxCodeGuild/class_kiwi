import re
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name = "chad"
    return render_template('index.html')

if __name__ == "__main__":
  app.run()

#  $env:FLASK_APP = "app.py"
#   $env:FLASK_ENV = "development"

    
@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html')   
    
@app.route('/check-grade') 
def check_grade():
    return render_template('check-grade.html')  


@app.route('llama', methods=['post'])
def display_name():
    name = request.form['username']   
    return render_template('contact.html', name=name)


