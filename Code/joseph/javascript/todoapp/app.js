//selectors
const todoBtn = document.querySelector('#todo-btn')
const todoInput = document.querySelector('#todo-input')
const todoList = document.querySelector('#todo-list')

//listeners
todoBtn.addEventListener('click', addTodo)
//todoInput.addEventListener('keypress', function(e){    console.log(e)})
todoInput.addEventListener('keypress', function(e){    
    if(e.key === 'Enter'){
        addTodo()
    }
})

//functions
function addTodo(){
    const todoText = todoInput.value

    const li = document.createElement('li')
    
    li.textContent = todoText

    todoList.appendChild(li)

    //create delete button, text = x
    const delBtn = document.createElement('button')
    delBtn.textContent = 'X'
    li.append(delBtn)

    //delete todo
    delBtn.addEventListener('click', function(){
        todoList.removeChild(delBtn.parentElement) //remove button from parent

    })

    //complete button
    const completeBtn = document.createElement('button')
    completeBtn.textContent = &#10004
    li.append(completeBtn)

    //complete todo
    completeBtn.addEventListener('click', function(){
        todoList.
    })

}
