// Selectors

const todoBtn= document.getElementById('todo-btn')
// ~either or~
// todoButton= document.querySelector('#todo-btn')
const todoInput= document.querySelector('#todo-input')
const todoList= document.querySelector("#todo-list")


// Listeners
todoBtn.addEventListener('click', addTodo)

todoInput.addEventListener('keypress',function(e){
// "event" or "e" : key for addEvent
    // console.log('event')
    // console.log(e)
    if(e.key === 'Enter'){
        addTodo()
    }

})
// ---------------------------------------------------------

// Function
function addTodo(){
    const todoText= todoInput.value
    // console.log(todoText)

// create <li></li>
    const li= document.createElement('li')
    // li.innerText = todoText
    // li.textContent = todoText
// create span
    const span= document.createElement('span')
    span.textContent = todoText
    li.append(span)


// append child to todoList
    todoList.appendChild(li)
    // clear input field
    todoInput.value= ''

// Delete button
    const delBtn= document.createElement('button')
    delBtn.textContent = 'X'
    // add delBtn as child to li
    // li.appendChild(delBtn)
    li.append(delBtn)
    // delete todo
    delBtn.addEventListener('click',function(){
        todoList.removeChild(delBtn.parentElement)
    })

// Complete button
    const completeBtn= document.createElement('button')
    completeBtn.textContent= '✔️'
    // append child
    li.append(completeBtn)

    //put checked todo at bottom of the list
    completeBtn.addEventListener('click',function(){
        const parent= completeBtn.parentElement
        
        const span= parent.querySelector('span')

        if(span.style.textDecoration === 'line-through'){
            span.style.textDecoration = 'none'
            span.style.color = 'black'
            todoList.insertBefore(parent, todoList.firstChild)
            completeBtn.textContent = 'check'
        }
        else{
            span.style.textDecoration = 'line-through'
            span.style.color = 'grey'
            todoList.removeChild(parent) // remove item from page
            todoList.append(parent) // re add to page
        }

        

    })


}
