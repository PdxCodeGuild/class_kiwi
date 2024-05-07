// null -> intentional
// undefined -> unintentional

var user = 'Tom'
// user = 'Person'


// console.log(user)

// variable names
// letter, numbers and symbols $ _

// var message= 'Hello class'
// message= 'Hello class'
// console.log(message)
// console.log(window.message)
// console.log(window)

// ---------------------------------------------------------------------------------------------

let day // declare
day= 'Tuesday' // initialize
// console.log(day)
day= 'Monday'
// console.log(day)

const age = 26 // declare + initialize
// age= 19 // Can NOT change const

// ---------------------------------------------------------------------------------------------

const numbers = [3,4] // (2) [3,4]

//push() 
// adds to the end of the array
numbers.push(5,6)
console.log(numbers) // (4) [3, 4, 5, 6]


// unshift() 
// adds to the beginning of the array
numbers.unshift(1,2)
console.log(numbers) // (6) [1, 2, 3, 4, 5, 6]

// splice()
// takes 3 arguments: (start, itemsToDelete, addItems)
numbers.splice(2,0,'a','b')
console.log(numbers) // (8) [1, 2, 'a', 'b', 3, 4, 5, 6]

const nums= [1,2,3,4]
console.log(nums) // (4) [1, 2, 3, 4]

// pop()
const last = nums.pop()
console.log(last) // 4
// shift()
// const first = nums.shift()
// console.log(first) // 1 

console.log(nums) // (2) [2, 3]

nums.push(7,9)
console.log(nums) //(4) [2, 3, 7, 9]

// nums.splice(1,2)
// console.log(nums) // (2) [2, 9]

console.log(nums.indexOf(9)) // 3
console.log(nums.indexOf('')) 

console.log(nums.includes(2)) //true
console.log(nums.includes(1)) // false

nums.push(3)
console.log(nums) // (5) [2, 3, 7, 9, 3]
console.log(nums.lastIndexOf(3))

// ---------------------------------------------------------------------------------------------
const courses= [
    {id:1, name:'a'},
    {id:2, name:'b'},
]


// callback functions

// const course= courses.find(function(course){
    // return course.name == 'a'

    // course = variable receive of value
    // courses= array of object
    // find() method
    // function(argument) "iterator"
    // function(course) is iterating over the objects within courses

    // })
    // console.log(course)

// arrow method

// const course= courses.find(course=>course.name=='b')

// console.log(course)


// const course= courses.findIndex(function(course){
//     return course.name == 'b'
// })
// console.log(course)

const first = [1,2,3]
const second = [4,5,6]
// const combined= first.concat(second)

// ----------------------------------------------

// spread operator ...
const combined = [...first, ...second]
// console.log(combined)

const copy = [...combined, 'item1', 'item2', ...first]
console.log(copy)

// ----------------------------------------------

const numbrs= [1,-1,2,3]


for(let i of numbrs){
    console.log(i)
}

// ----------------------------------------------

// numbrs.forEach(function(x, index){
    //     console.log(x, 'x', index, "index")
    // })
    
numbrs.forEach((number,index)=> console.log(index,number, 'like enumerate'))
    
console.log(numbrs) // (4) [1, -1, 2, 3]
    
// ----------------------------------------------

// const filtered= numbrs.filter(function(value){
    //     return value >=0
    // })
    // console.log(filtered) // (3) [1, 2, 3]
    
    const filtered= numbrs.filter(x=> x>=0)
    console.log(filtered) //(3) [1, 2, 3]
    
    
// ------------------------------------------------------------------------------------------------

function getFullName(title, fname, lname, degree){
    return `${title} ${fname} ${lname} ${degree}`
}

let test = getFullName('Dr','John','Smith','MD')
console.log(test)

function showYourWork(num1,num2){
    return `${num1}+${num2}=${num1+num2}`
}
let value = showYourWork(2,3)
console.log(value)

let text = 'hello'
console.log(text[0])
console.log(text[1])
console.log(text.charAt(4))

// let s= 'hello'+' '+'world' // hello world
// s= 'hello'.concat(' ', 'world') // hello world
// console.log(s)

// let s = 'hello '
// console.log(s.repeat(5))

let s= 'hello world, hello people'
console.log(s) 

console.log(s.indexOf('hello')) // 0
console.log(s.lastIndexOf('hello')) // 13
console.log(s.includes('hello')) // true
console.log(s.startsWith('hello')) // true
console.log(s.endsWith('people')) // true

console.log(s.toLocaleUpperCase())

console.log(s.toLowerCase())

// s= s.replace('hello','goodbye')
// console.log(s) // goodbye world, hello people

s= s.replaceAll('hello','goodbye')
console.log(s) // goodbye world, goodbye people

//-------------------------------------------------------------------------------------------------

let fruits = 'apples plums grapes'

fruits= fruits.split(' ')
console.log(fruits) // (3) ['apples', 'plums', 'grapes']

console.log(fruits.join(' ')) // apples plums grapes

s = 'hello world'
console.log(s.substring(1,5)) // ello
console.log(s.slice(1,5)) // ello

let list = [0,1,2,3,4,5,6,7,8,9]

for(let i=0; i<list.length; i++){
    if(list[i] == 6){
        break
    }
    console.log(list[i])
}


