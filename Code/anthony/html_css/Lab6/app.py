from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def result():
    distance = request.form['distance']
    unit = request.form['unit']
    distance = int(distance)

    conversion_list = [0.3048, 1609.34, 1, 1000, 0.9144, 0.0254]
    if unit == 'feet':
        total = distance * conversion_list[0]
    elif unit == 'miles':
        total = distance * conversion_list[1]
    elif unit == 'meter':
        total = distance
    elif unit == 'km':
        total = distance * conversion_list[3]
    elif unit == 'yard':
        total = distance * conversion_list[4]
    elif unit == 'inch':
        total = distance * conversion_list[5]

    return render_template('results.html', unit=unit, distance=distance, total=total)
