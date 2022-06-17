// const headers = document.getElementsByTagName('h2')
// console.log(headers)
// console.log(headers[1])

// const list = document.getElementsByClassName('item')
// console.log(list)

// const button = document.getElementById('submit') //getElementById gets first instance of given Id
// console.log(button)

// const headers = document.querySelectorAll('h2')
// console.log(headers)

// const list = document.querySelectorAll('.item') // reference classes with .classname, id with #id
// console.log(list)

// const list = document.querySelector('#list a')
// console.log(list)

//SELECTORS
// const button = document.querySelector('#submit')


//LISTENERS
// button.addEventListener('click', function(){
//     console.log('Test Button')
// })

// button.addEventListener('click', addItem)
// function addItem(){
//     console.log('Test Button')
// }

//SELECTORS
const button = document.querySelector('#submit')
const todoList = document.querySelector('#todo-list')
const todoItems = todoList.children
const todoNum = document.querySelector('.todo-num b')
const mainTitle = document.querySelector('.main-title')
const nameInput = document.querySelector('.name-input')

//LISTENERS
button.addEventListener('click', function(e){
    e.preventDefault()
    const newItem = document.createElement('li')
    newItem.classList.add('item')
    // newItem.innerText = `Item ${todoItems.length + 1}`
    newItem.innerText = nameInput.value
    todoList.appendChild(newItem)
    nameInput.value = ''

    newItem.addEventListener('click', deleteItem)
})

button.addEventListener('click', function(){     mainTitle.style.color = 'blue'
    mainTitle.style.fontSize = '2.5rem'
})

// for (item of items){
//     item.addEventListener('click', deleteItem)
// }

todoList.addEventListener('click', function(){
    todoList.classList.toggle('fade')

})


function deleteItem(e){
    // console.log(e)
    // console.log(e.target)
    e.stopPropagation()
    e.target.remove()
    todoNum.innerText = todoItems.length
}