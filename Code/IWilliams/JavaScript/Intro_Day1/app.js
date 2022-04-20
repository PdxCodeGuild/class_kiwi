//alert('Hello World')
// console.log('Hello class Kiwi') 
// console.warn('something is up')
// console.info('Page Loaded')

// let color 
// color = 'blue'
// console.log(color)

// color = 'yellow'
// console.log(color)
// color = 'red'
// console.log(color)

// const favColor = 'blue'
// console.log(favColor, 'fav color')
// favColor = 'pink'

// const socialSecNum = 12134646676
// let lastName = 'Smith'

// let color = 'bluegreen'
// console.log(typeof color)

// let numberOne =1
// console.log(typeof 1)

//Data types
// 'Hello World' //String
// "Hello World" //String
// 4             //Number 
// 4.7           //Number 
// true           //Boolean
// [1,2,3]        //Array 
// {name: 'Tom'}  //Object
// undefined      //undefined (value does not exits)
// null           // intentional absence of the value   

// //let x = '24'+"Tomorrow"
// let x = + 6 +24+"Tomorrow" 
// console.log(x) //246Tomorrow

// let number = 5
// console.log(number ==='5') 

// let a =1 // number (Js) --> integer
// let b = 1.2 //number (JS) --> float, decimal
// let c = 123e7 //large number
// let d = 123e-7 //sci not
// console.log(typeof a)

// let number = 10
// if (number<10){
//    console.log("hooray!") 
// }else if(number>11){
//     console.log('this is a large number')
// } else{
//     console.log('testing')
// }

// let person = {
//     firstName: 'Jackson',
//     lastName: 'Brown',
//     age: 30
// }
// console.log(person)
// console.log(person['firstName'], 'square bracket')
// console.log(person.lastName)
// console.log(person.age)

// //update age
// person.age =40
// console.log(person.age)

// //increment by 1
// person.age +=1
// console.log(person.age)

// //increment by ++
// person.age ++
// console.log(person.age)

// //increment by +=2
// person.age +=2
// console.log(person.age)


// let person = {
//         firstName: 'Jackson',
//         lastName: 'Brown',
//         age: 30,
//     pets:{
//         dog: 'Spot',
//         cat: 'Ginger',
//         rock: 'Rocky'
//     }
// }   
// console.log(person)
// console.log(person['pets'])
// console.log(person.pets)

// let colors = {
//     'red': '#FF0000',
//     'green': '#00FF00',
//     'blue': '#0000FF'
// }

// for(key in colors){
//     console.log(colors[key])
// }

// // console.log(Object.keys(colors))
// // console.log(Object.values(colors))
// for(const [key, value] of Object.entries(colors)){
//     console.log(`${key}: ${value}`) //f'{}'
// }

// let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato']
// //for of loop
// for(pie of pies){
//     console.log(pie)
//     //console.table(pie)
// }
//for in loop 'in for index'
// for(pie in pies){
//     console.log(pie)
// }

//push
// pies.push('Shepard')
// pies.push('Blueberry')
//console.log(pies)

//pop
// let bestPie =  pies.pop()
// console.log(bestPie)

//include method 
// if(pies.includes('Blueberry')){
//     console.log('We have a pumpkin pie')
// }

console.log(pies)
updatedArray = pies.splice(2, 2)
console.log(updatedArray)
console.log(pies)
//console.log(pies.slo)

//splice starts at index 1 and stop at index 1
pies.splice(1,1)
console.log(pies)

// let stringPies = pies.join('-')
// console.log(stringPies)

let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato']

// for(let i=0; i<100; i++){
//     console.log(i)

// }

// for(let i=0; i<pies.length; i++){
//     console.log(i)
//     pies[i] = 'X'
//     console.log(pies)
// }

// pies.forEach(function(pie){
//     console.log(pie)
// })


// function sayHello(){
//     let color = 'blue'
//     return color
// }
// console.log(sayHello())

//traditional 
function addNums(num1, num2, num3=3){
    return num1 + num2 + num3
}
console.log(addNums(3, 2))

// const arrowFunct = (num1, num2) => {
//     return num1 + num2
// }
// console.log(arrowFunct(2,7))