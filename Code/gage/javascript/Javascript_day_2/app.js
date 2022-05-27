// var user = 'Gage'
// console.log(user)

// // valid
// var user2
// var user$
// var $user
// var user_
// //invalid
// var 2user




// message = 'Hello class kiwi' // causes problems
// console.log(window)
// console.log(message)

// let message = 'Hello class KIWI' // correct!
// console.log(window)
// console.log(message)



// let day = 'Tuesday'
// console.log(day)
// day = 'Wednesday'
// console.log(day)

// const color = 'red'
// console.log(color)
// color = 'blue'
// console.log(color)
// Let allows you to update the value while const does not


// push()                       MEHTOD 

// const nums = [3,4]
// console.log(nums)
// nums.push(5, 6)
// console.log(nums)

//unshift()                     METHOD

// nums.unshift(1,2)
// console.log(nums)

// splice()                     METHOD

// nums.splice(2, 0, 'a','b')
// console.log(nums)

// pop()                        METHOD
// const nums = [1,2,3,4]
// console.log(nums)
// const last = nums.pop()
// console.log(last)
// console.log(nums)

// // shift() METHOD
// const first = nums.shift()
// console.log(first)
// console.log(nums)

// // console.log(nums.indexOf(2) + ' - The ^ index number of 2')
// // console.log(nums.includes(10) + ' - Array does not include 10')

// const courses = [ // Array of objects
//     {id: 1, name:'a'},
//     {id: 2, name:'b'},
//     {id: 3, name:'c'},
// ]

// // // find()                   MEHTHOD
// // const course = courses.find(function(course){
// //     return course.name == 'c'
// // })

// // console.log(course)
// // const course = courses.find(course => course.name=='b')
// const course = courses.findIndex(function(course){
//     return course.name == 'b'
// })
// console.log(course)

// concat()             METHOD
// const first = [1,2,3]
// const second = [4,5,6]
// // const combine = first.concat(second)

// const combine = [... first, 'car', ...second]
// console.log(combine)

// const nums = [1,2,3,4,5]

// for(let num of nums){
//     console.log(num)
// }

// nums.forEach(function(num, index){              //Enumerate
//     console.log(index, num)
// // })

// // nums.forEach((num, index)=> console.log(index, num))
// const nums = [1,-1, 2, 3]

// // const filtered = nums.filter(function(value){
// //     return value >= 0
// // })

// const filtered = nums.filter(x=> x>=0)
// console.log(filtered)

// function getFullName(title, fname, lname, degree){
//     return `${title} ${fname} ${lname} ${degree}`
// }

// function showYourWork(num1, num2){
//     math = num1 + num2
//     return `${num1} + ${num2} = ${math}`
// }


// console.log(showYourWork(4, 6))
// console.log(getFullName('Mr.', 'gage', 'lieble', 'bootcamp'))


// let text = 'hello'
// console.log(text[0])
// console.log(text[1])
// console.log(text[2])
// console.log(text[3])
// console.log(text.charAt(4))

// // let s = text + ' ' + 'world'
// // console.log(s)

// s = text.concat(' ', 'world')
// console.log(s)

// let s = 'hello '
// console.log(s.repeat(10))

// let s = 'hello world, hello sun'
// console.log(s)
// console.log(s.indexOf('hello'))
// console.log(s.lastIndexOf('hello'))
// console.log(s.includes('hello'))
// console.log(s.includes('moon'))
// console.log(s.startsWith('hello'))

// let fruits = 'apples plums grapes'
// fruits = fruits.split(' ')
// console.log(fruits)

let nums = [0,1,2,3,4,5,6,7,8,9]
for(let i=0; i<nums.length; i++ ){
    if (nums[i]%2 == 1){
        continue
    }
    console.log(nums[i])
}
