const todoInput = document.querySelector('#todo-input')
const todoBtn = document.querySelector('#todo-btn')
const todoList = document.querySelector('#todo-list')

todoBtn.addEventListener('click', addItem)
todoInput.addEventListener('keypress', function(event){
    console.log(event)
    if(event.key === 'Enter'){
        addItem()
    }
})

function addItem(){
    const newItem = todoInput.value
    console.log(newItem)
    const li = document.createElement('li')
    todoList.append(li)
    li.append(newItem)

    const delBtn = document.createElement('button')
    delBtn.textContent = 'del'
    li.append(delBtn)
    delBtn.addEventListener('click', function(){
        todoList.removeChild(delBtn.parentElement)  // remove button from parent
    })

    const complete = document.createElement('button')
    complete.textContent = '☑'
    li.append(complete)
    complete.addEventListener('click', function(){
        li.style.textDecoration = 'line-through'
    })
}