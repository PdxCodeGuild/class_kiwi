from flask import Flask, render_template

app = Flask(__name__)


#localhost:5000/
@app.route('/')
def index():         

    return render_template('index.html')


#run flask app by below command inputs
#$env:FLASK_APP= "app.py"
#py -m flask run
#You will need to run the flask app each time to refresh your page...1st kill your terminal by Ctrl + C then type py -m flask run


#change the location of the webpage ..change the name from home to - /about 
#previous route was just 5000/ which routed to index.html
@app.route('/about')
def about():
   
    return render_template('about.html')


