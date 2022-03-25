from flask import Flask

app = Flask(__name__)



#localhost:5000/
@app.route('/')
def index ():
    return 'Hello World'
@app.route('/about')
def about():
    return 'This is the about page!'

if _name__ == "__main__":
    app.run(debug=True)
