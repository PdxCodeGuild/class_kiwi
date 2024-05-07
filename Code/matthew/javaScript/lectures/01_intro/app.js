// alert('hello world')

// similar to python print()

// console.log('hello Class')
// console.warn('something is up')
// console.info('Page Loaded')

// let userInput = prompt('how is your day?')
// alert(userInput)

let color= 'yellow'
// yellow in terminal
console.log(color)
color = 'red'
// red in console
console.log(color)

const favColor = 'blue'
// blue fave color in console
console.log(favColor, 'fav color')
// favColor = 'pink'

// you cant change variable using const
const socialSecNum= 123456
// can change the variable set using let
let lastName= 'Smith'

// console.log(typeof color)

// let numberOne= 1
// console.log(typeof 1)

// --------------------------------------------------------------------------------------------------------

//Data Types
'hello World'   // String
"hello World"   // String
4               // Number
4.7             // Number
true            // Boolean
[1,2,3]         // Array
{name:'Tom'}    // Object (Js) --> dict (py)
undefined       // undefined (value does not exist)
null            // intentional absence of value
                // ex: year == null

// let x = '24' + "Tomorrow"
// console.log(x) // 24Tomorrow
// console.log(typeof x) // string


// Type coercion // javaScript converts 24 into a string

// let x = 24 + 'Tomorrow'
// console.log(x) // 24Tomorrow

// javaScript ignores extra +
// let x = 24 + + 6 + 'tomorrow'
// console.log(x) //30tomorrow

let number = 5
console.log(number == '5') //true //  implicit relationship: javaScript auto converts '5' string to number 5
console.log(number === '5') //false // explicit relationship: javaScrip is looking for an exact match

// ------------------------------------------------------------------------------------------------

// numbers in javaScript are all numbers
let a= 1 // number (Js) --> integer (py)
let b= 1.2 // number (Js) --> float (py)
let c= 123e7 // larger number
let d= 123e-7 // larger negative number

let num= 11
if (num<10){
    console.log('number is less then 10')
}
else if(num>12){ // elif statement
    console.log('number is greater than 12')
}
else {
    console.log('number is between 10 - 12')
}

// Objects----------------------------------------------------------------------------------------------

// objects
// key:value
let person = {
    firstName: 'Jackson',
    lastName: 'Brown',
    age: 30,
    pets:{
        dog: 'spot',
        cat: 'ginger',
        rock: 'rocky',
    }
}

console.log(person)
console.log(person['firstName'], 'square bracket "firstName"')
console.log(person.lastName, 'person.lastName')

// update age
person.age = 40
console.log(person)
console.log(person.age)

// // increment age using += 1
// person.age += 1
// console.log(person.age)

// increment age using ++ : increases age by 1
// person.age ++
// console.log(person.age)

console.log(person.pets)

let colors = {
    'red': '#ff0000',
    'green': '#00ff00',
    'blue': '#0000ff'
}

for(key in colors){
    console.log(colors[key])
}

console.log(Object.keys(colors))
console.log(Object.values(colors))

for(const [key, value] of Object.entries(colors)){
    console.log(`${key}:${value}`) // (py) -->: f'{variable_name}'
}

// Array-------------------------------------------------------------------------------------------------

// Array
let pies = ['Apple','Pumpkin', 'Pecan', 'Sweet Potato']

// for of loop
for(pie of pies){
    console.log(pie) // returns object at index position
    // console.log(`${pie}`)
}

// for in loop 'in for index'
for(pie in pies){
    console.log(pie) // returns index position of object
}

// add item to array

// push()
pies.push('Peach')
pies.push('Blueberry')
console.log(pies)

// remove item of array

// pop() removes last item of array
let bestPie= pies.pop()
console.log(bestPie) // returns Blueberry


// include method

// if pies array contains Pumpkin
if(pies.includes('Pumpkin')){
    console.log('it has pumpkin')
}

// slice() makes a copy

// grab a copy starting at index 2 and ends at index 3
i =pies.slice(2,3)
console.log(i, 'checking slice')
console.log(pies) // (5) ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato', 'Peach']

// splice() removes items

// starts at index 2 and removes 1 instance 
x = pies.splice(2,1)
console.log(x,"checking splice") // ['Pecan'] 'checking splice' 
console.log(pies) // (4) ['Apple', 'Pumpkin', 'Sweet Potato', 'Peach']

// .join() joins the array and returns a string
let stringPies= pies.join(',')
// console.log(stringPies)

// console.log(pies) // (4) ['Apple', 'Pumpkin', 'Sweet Potato', 'Peach']


// for(let i=0; i<100; i++){

// prints i in range 100
// i ++ increases i by one 1 per loop
for(i=0; i<100; i++){
// console.log(i)
}

// for(let i=0; i<pies.length; i++){
//     console.log(i,pies[i])
//     pies[i] = 'X'
//     console.log(pies)
// }

// array method +
// anonymous function(pie)
pies.forEach(function(pie){
    console.log(pie) // returns object at each index similar to a for of loop
})


// Functions---------------------------------------------------------------------------------------------------

function sayHello(){
    let color = 'blue'
    return color
}
// console.log(sayHello()) // 'blue'

function addNums(x,y){
    return x+y
}
console.log(addNums(2,2,6))

const arrowFunct = (num1, num2) => {
    return num1 + num2
} 