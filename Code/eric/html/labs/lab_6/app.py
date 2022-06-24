from crypt import methods
from unittest import result
from flask import Flask, render_template, request

app = Flask(__name__)

# route items to the index
@app.route('/')
def index():
    return render_template('index.html')

#route the actual application
@app.route('/converter', methods = ['POST'])
def convertor():
    result = request.form
    
    user = result['measure_in']
    
    conversion_in = {
    'ft' : .3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000
}

conversion_out = {
    'ft' : 1/.3048,
    'mi' : 1/1609.34,
    'm' : 1,
    'km' : 1/1000
}

#build input
distance=input("what is the distance? ")
distance=int(distance)

unit_in=input("what are the input units? choose ft, mi, km: ")
unit_out=input("what are the output units? choose ft, mi, km: ")

#enter sausage maker
if unit_in in conversion_in and unit_out in conversion_out:
    converted_to_meters = conversion_in[unit_in]
    distance_in_meters = converted_to_meters * distance
    meters_out = conversion_out[unit_out]
    final_conversion = meters_out * distance_in_meters
    print(f"{distance}{unit_in} is {round(final_conversion,4)}{unit_out}")

else:
    print("unit not recognized")
    
    return render_template('results.html', user=user)