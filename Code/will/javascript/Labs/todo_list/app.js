const button = document.querySelector("#submit")
const todoList = document.querySelector('#todo-list')
const todoItems = todoList.children
const nameInput = document.querySelector('.name-input')
const taskList = document.getElementsByTagName('li')

//LISTENERS
button.addEventListener('click', function(e){
    e.preventDefault()
    const newItem = document.createElement('li')
    newItem.classList.add('item')
    newItem.innerText = nameInput.value
    todoList.appendChild(newItem)
    nameInput.value = ''

    newItem.addEventListener('dblclick', deleteItem)
})

todoList.addEventListener('click', function(){
    todoList.classList.toggle('fade')

})

todoList.addEventListener('click', function(){
    
})

todoList.addEventListener('click', markComplete)

function deleteItem(e){
    e.stopPropagation()
    e.target.remove()
}

function markComplete(e){
    e.stopPropagation()
    e.target.style.setProperty("text-decoration", "line-through")
}