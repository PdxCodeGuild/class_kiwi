// var user = "Lisa"
// //user = "Lisa"
// console.log(user)

//letter, numbers and symbols $ _
//invalid
// var user$
// var user2
// var user2_
// var $user2_

// message = 'hello class kiwi'
// console.log(window.message)
// console.log(message)

// window.console.log('hello')
// console = 'hello'
// console.log('hello')

// let day //declare
// //day = 'Tuesday' //initialize
// // console.log(day)
// // day  = 'Friday'
// // console.log(day)

// const age =32
// age =35

// const numbers =[3,4]
// console.log(numbers)
// numbers.push(5,6)
// console.log(numbers)

// //unshift()
// numbers.unshift(1,2)
// console.log(numbers)

// numbers.splice(2, 1, 'a', 'b')
// console.log(numbers)

// numbers.splice()

// const numbers =[1,2,3,4]
// console.log(numbers)
// const last = numbers.pop()
// console.log(last)

// const first = numbers.shift()
// console.log(first)
// console.log(numbers)

// //splice
// numbers.push(7,9)
// console.log(numbers)
// // numbers.splice(1, 2)
// // console.log(numbers)
// console.log(numbers.indexOf('2'))
// console.log(numbers.indexOf(9))
// console.log(numbers.includes(10))

// numbers.push(3)
// console.log(numbers)
// console.log(numbers.lastIndexOf(3))

// const courses =[
//     {id:1, name:'a',},
//     {id:2, name:'b'}
// ]

// // const course = courses.find(function(course){
// //     return course.name === 'a'  
// //     //course.name +=1
// //     //course = name.c return 

// //     //course = variable receive of value 
// //     //courses = array of object 
// //     //find() method
// //     //function(course.)
// // })
// //const course =courses.find(course=>course.name==='b')
// const course = courses. findIndex(function(course){
//     return course.name==='b'
// })
// console.log(course)

// const first = [1,2,3]
// const second = [4,5,6]
// //const combined = first.concat(second)
// const combined = [...first, 'car', 'bike',...second, 'last']
// console.log(combined)

// const copy = [...combined]
// console.log(copy)

// const numbers = [1,2,3,4,5]

// for(let number of numbers){
//     console.log(number)
// }

// numbers.forEach(function(number, index){
//     console.log(index, number)
// })

// numbers.forEach((number, index) => console.log(index, number))

// const numbers = [1, -1, 2, 3, 9, 0, -8]  //[1, 2, 3 ]
// // const filtered = numbers.filter(function(value){
// //     return value >=0
// // })

// const filtered = numbers.filter(x=> x>=0)
// console.log(filtered)

// function getFullName(title, fname, lname, degree){
//     return `${title} ${fname} ${lname} ${degree}`
// }
// let value = getFullName('Dr.', 'John', 'Smith', 'Msc')
// console.log(value)

// function showYourWork(num1, num2){
//     return `${num1} + ${num2}  = ${num1 + num2}`
// }

// let value2 = showYourWork(3, 4)
// console.log(value2)

// let text = 'hello'
// console.log(text[0])
// console.log(text[1])
// console.log(text.charAt(4))

// let s = 'hello' + ' ' + 'world'
// console.log(s)

// let s = 'hello'.concat(' ', 'world')
// console.log(s)

// let s = 'hello '
// console.log(s.repeat(10))

// let s = 'hello world, hello moon'
// console.log(s)
// console.log(s.indexOf('hello'))
// console.log(s.lastIndexOf('hello'))
// console.log(s.includes('hello'))
// console.log(s.includes('goodbye'))
// console.log(s.startsWith('goodbye'))
// console.log(s.endsWith('moon'))
// console.log(s.toUpperCase())
// console.log(s.toLowerCase())
// // s = s.replace('hello', 'goodbye')
// s = s.replaceAll('hello', 'goodbye')
// console.log(s)

//covert string 2 array
// let fruits = 'apples plums grapes'
// fruits = fruits.split(' ')
// console.log(fruits)

//convert array 2 string
// let fruits = ['apples', 'plums',  'grapes']
// fruits = fruits.join(', ')
// console.log(fruits)

// let s = 'hello world'
// console.log(s.substring(1, 5))
// console.log(s.slice(1, 5))

// let nums = [0,1,2,3,4,5,6,7,8,9]
// for (let i=0; i<nums.length; i++){
//     if (nums[i]==3){
//         break
//     }
//     console.log(nums[i])
// }

let nums = [0,1,2,3,4,5,6,7,8,9]
for (let i=0; i<nums.length; i++){
    if (nums[i]==5){
        continue
    }
    console.log(nums[i])
}