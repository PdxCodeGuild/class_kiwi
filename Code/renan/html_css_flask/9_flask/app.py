from flask import Flask, render_template

app = Flask(__name__)


#localhost:5000/
@app.route('/')
def index():
    name = "Bill"
    return render_template('index.html', name=name)

#$env:FLASK_APP= "app.py"

@app.route('/about')
def about():
    return render_template('about.html')