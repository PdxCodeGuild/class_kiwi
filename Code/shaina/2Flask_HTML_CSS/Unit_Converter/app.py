from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    result = request.form

    unit1= result['s_unit']
    unit2= result['e_unit']
    dist = float(result['distance'])
    units_to_m = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
    }
    conversion = round((dist * units_to_m[unit1]) * (1/units_to_m[unit2]), 4)

    return render_template('results.html',unit1=unit1, unit2=unit2, dist=dist, conversion=conversion)