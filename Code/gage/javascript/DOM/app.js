// const headers = document.getElementsByTagName('h2')
// const list = document.getElementsByClassName('item')
// const button = document.getElementById('submit')
// const headers = document.querySelector('h2') // ONLY ALLOWS 1 OBJBECT
// const headers = document.querySelectorAll('h2') // Selecets ALL matching Objects
// const list = document.querySelectorAll('.item')
// const list = document.querySelector('#list a')
// console.log(list)
// console.log(headers)

// Selectors
// const button = document.querySelector('#submit')

// Listeners
// button.addEventListener('click', addItem)

// function addItem(){
//     console.log("Test gg")
// }

// button.addEventListener('click', function(){
//     console.log("Test Button")
// })










// HTML HTML HTML HTML HTML HTML HTML HTML HTML HTML HTML 

// Selectors
const button = document.querySelector('#submit')
const todoList = document.querySelector('#todo-list') // selects Parent
const items = todoList.children // selects Children
const todoNum = document.querySelector('.todo-num b')
// Listeners

button.addEventListener('click', function(){
    const newItem = document.createElement('li')
    newItem.classList.add('item')
    // const count = 1 + items.length
    // newItem.innerText = 'Item ' + count
    newItem.innerText = `Item ${items.length + 1}`
    todoList.appendChild(newItem)
    todoNum.innerText = items.length
    console.log(newItem)
})


// CSS CSS CSS CSS CSS CSS CSS CSS CSS CSS CSS CSS CSS CSS

const mainTitle = document.querySelector('.main-title')

button.addEventListener('click', function(){
    // mainTitle.style.color = 'blue'
    // mainTitle.style.fontSize = '50px'
    mainTitle.classList.add('new-style')


})