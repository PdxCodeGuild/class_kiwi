let body = document.body
let unit = prompt('Enter a unit of measure: inches, feet, meters, yards, kilometers, miles')
let number = prompt('Enter number to be converted')
console.log(unit);
console.log(number);

let values =  {"feet": 0.3048,
                "miles": 1609.34,
                "meters": 1,
                "kilometers": 1000,
                "yards": 0.9144,
                "inch:": 0.0254
}


let unitValue = values[unit];
let change = unitValue * number;
body.append(`Your input ${unit},
 conversion: ${change} meters.`);


document.body.style.backgroundColor = "tan";


document.body.style.font = "italic bold 25px arial,serif";


document.getElementById("border").style.borderTop = "thick solid #0000FF";