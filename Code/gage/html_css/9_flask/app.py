from flask import Flask, render_template, request
app = Flask(__name__)

# localhost:5000/    -- Checks for the '/' on the local host 5000 server
@app.route('/') 
def index():
    name = "tester"
    return render_template("index.html", name=name)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/grade/<int:grade>")
def grade(grade):
    return render_template("check_grade.html", grade=grade)

@app.route("/llama", methods=['post'])
def llama():
    social = request.form["social_num"]
    return render_template("social.html", social=social)