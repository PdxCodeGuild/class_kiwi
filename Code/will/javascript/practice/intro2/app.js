// var user
// user = 'Lisa'

// console.log(user)

// Js variables accept letters, numbers (not leading), and % _ symbols

// message = 'Hello World'
// console.log(window)
// console.log(window.message)

// window.console.log('hello')
// console = 'hello'
// console.log('hello')

// let day
// day = 'Tuesday'
// console.log(day)
// day = 'Friday'
// console.log(day)

// const numbers = [3,4]

// numbers.push(5,6)
// console.log(numbers)

// numbers.unshift(1,2)
// console.log(numbers)

// numbers.splice(2,0,'a','b')
// console.log(numbers)

// const numbers = [1,2,3,4]
// console.log(numbers)
// const last = numbers.pop()
// console.log(last)

// const first = numbers.shift()
// console.log(first)
// console.log(numbers)

// numbers.push(7,9)
// console.log(numbers)
// // numbers.splice(1, 2)
// // console.log(numbers)
// console.log(numbers.indexOf('2'))
// console.log(numbers.indexOf(9))
// console.log(numbers.includes(2))

// numbers.push(3)
// console.log(numbers)
// console.log(numbers.lastIndexOf(2))

const courses = [
    {id: 1, name: 'apple'},
    {id: 2, name: 'banana'},
    {id: 3, name: 'pear'}
]

const course = courses.find(function(course){
    return course.name === 'apple'
})
console.log(course.name)