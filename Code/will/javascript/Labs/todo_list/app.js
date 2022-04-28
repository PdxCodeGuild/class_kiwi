const button = document.querySelector("#submit")
const todoList = document.querySelector('#todo-list')
const todoItems = todoList.children
const nameInput = document.querySelector('.name-input')

//LISTENERS
button.addEventListener('click', function(e){
    e.preventDefault()
    const newItem = document.createElement('li')
    newItem.classList.add('item')
    newItem.innerText = nameInput.value
    todoList.appendChild(newItem)
    nameInput.value = ''

    newItem.addEventListener('click', deleteItem)
})

todoList.addEventListener('click', function(){
    todoList.classList.toggle('fade')

})


function deleteItem(e){
    // console.log(e)
    // console.log(e.target)
    e.stopPropagation()
    e.target.remove()
}