//selectors

const todoBtn = document.querySelector('#todo-btn')
const todoInput = document.querySelector('#todo-input')
const todoList = document.querySelector('#todo-list')
//listeners
todoBtn.addEventListener('click', addTodo)
todoInput.addEventListener('keypress', function(e){
    // console.log(e)
    if(e.key === 'Enter'){
        addTodo()
    }
})


//function
function addTodo(){
    const todoText = todoInput.value
    const li = document.createElement('li')
    li.textContent = todoText

    //create span 
    const span = document.createElement('span')
    span.textContent = todoText
    li.append(span)


    todoList.appendChild(li)
    todoInput.value = '' // clear data

    //create delete button, text = X
    const delBtn = document.createElement('button')
    console.log(delBtn)
    delBtn.textContent = 'X'
    li.append(delBtn)

    //delete todo
    delBtn.addEventListener('click', function(){
            todoList.removeChild(delBtn.parentElement) // remove button from parent

    }) 

    //complete button
    const completeBtn = document.createElement('button')
    completeBtn.textContent = '☑'
    li.appendChild(completeBtn)

    //put checked todo at bottom of list
    completeBtn.addEventListener('click', function(){
        const parent = completeBtn.parentElement

       
        const span = parent.querySelector('span')
        if (span.style.textDecorationo === 'line-through'){
            span.style.textDecoration = 'none'
            span.style.color = 'black'
            todoList.insertBefore(parent, todoList.firstChild)
            completeBtn.textContent = '☑'
        }else{
            span.style.textDecoration = 'line-through'
            span.style.color = 'gray' 
            todoList.removeChild(parent) // remove item from page 
            todoList.append(parent)
        }
    })
}

