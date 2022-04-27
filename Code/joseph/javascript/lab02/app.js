const todoInput = document.querySelector('#todo-input')
const todoBtn = document.querySelector('#todo-button')
const todoList = document.querySelector('#todo-list')

todoBtn.addEventListener('click', createTodo)
todoInput.addEventListener('keypress', function(e){
    if(e.key === 'Enter'){
        createTodo()
    }
})

function createTodo(){
    const todoText = todoInput.value
    const li = document.createElement('li')

    li.textContent = todoText

    todoList.appendChild(li)

    const deleteBtn = document.createElement('a')
    deleteBtn.setAttribute('href', "#")
    deleteBtn.setAttribute('role', "button")
    deleteBtn.setAttribute('class', "contrast outline")
    deleteBtn.innerText = 'X'
    li.append(deleteBtn)

    deleteBtn.addEventListener('click', function(){
        todoList.removeChild(deleteBtn.parentElement)
    })

    const completeBtn = document.createElement('a')
    completeBtn.setAttribute('href', "#")
    completeBtn.setAttribute('role', "button")
    completeBtn.setAttribute('class', "primary outline")
    completeBtn.innerHTML = "&#10003;"
    li.append(completeBtn)

    completeBtn.addEventListener('click', function(){
        li.removeChild(deleteBtn)
        li.removeChild(completeBtn)
        let text = li.textContent
        li.innerHTML = "<s>"+text+"</s>"
    })
}
