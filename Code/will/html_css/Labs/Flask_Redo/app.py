from flask import Flask, render_template, request
app = Flask(__name__)

# localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['post'])
def results():
    conversion = request.form

    units_to_convert = conversion['convert']
    distance_to_convert = conversion['amount']
    meters_to_units = conversion['converted']
    distance_to_convert = int(distance_to_convert)

    distances = {'feet': 0.3048, 'miles': 1609.34, 'meters': 1.0, 'kilometers': 1000, 'yards': 0.9144, 'inches': 0.0254}
    units_to_meters = distance_to_convert * distances.get(units_to_convert)                                                                                   # convert the meters into the desired second unit and print results
    converted_units = units_to_meters / distances.get(meters_to_units)
    converted_units = round(converted_units, 3)

    return render_template('results.html', converted_units=converted_units, meters_to_units=meters_to_units, units_to_convert=units_to_convert, distance_to_convert=distance_to_convert)