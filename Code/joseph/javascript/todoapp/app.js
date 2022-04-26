//selectors
const todoBtn = document.querySelector('#todo-btn')
const todoInput = document.querySelector('#todo-input')
const todoList = document.querySelector('#todo-list')

//listeners
todoBtn.addEventListener('click', addTodo)

//functions
function addTodo(){
    const todoText = todoInput.value
    console.log(todoText)

    const li = document.createElement('li')
    console.log(li)
    
    li.textContent = todoText

    todoList.appendChild(li)
}
