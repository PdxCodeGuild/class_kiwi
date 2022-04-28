let body = document.body;
let unit = prompt('Enter one of the following units, inches, feet, meters, yards, kilometers, miles').toLowerCase();
let amount = prompt('Enter a number for the previous unit that you would like converterd to meters: ');

console.log(unit);
console.log(amount);


let values = {
    'inches':0.0254,
    'feet':0.3048,
    'meters':1,
    'yards':0.9144,
    'kilometers':1000,
    'miles':1609.34,
}

let unitNumber = values[unit];
let conversion = unitNumber * amount;
body.append(`You picked ${amount} ${unit}, we converted that into ${conversion} meters.`);