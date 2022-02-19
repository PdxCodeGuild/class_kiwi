units = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000,
"yd": 0.9144,
"in": 0.0254
}
distance = int(input("\nWhat is the distance? "))
unit = input("What are the units 'ft', 'mi', 'm', 'km', 'yd', or 'in'? ")
for key in units:
    if key == unit:
        output = units[key] * distance
        print(f"\n{distance} {unit} is {output:.2f} m\n")
        break