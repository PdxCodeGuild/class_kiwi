units = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000,
"yd": 0.9144,
"in": 0.0254
}
distance = float(input("\nWhat is the distance? "))
input_unit = input("What are the input units 'ft', 'mi', 'm', 'km', 'yd', or 'in'? ")
output_unit = input("What are the output units 'ft', 'mi', 'm', 'km', 'yd', or 'in'? ")
for key in units:
    if key == input_unit:
        to_unit = units[key] * distance
for key in units:
    if key == output_unit:
        from_unit = to_unit / units[key]
        print(f"\n{distance} {input_unit} is {from_unit} {output_unit}\n")