// selectors
const todoBtn = document.querySelector('#todo-button')
const todoInp = document.querySelector('#todo-input')
const todoList = document.querySelector('#todo-list')

// listeners
todoBtn.addEventListener('click', addTask)
todoInp.addEventListener('keypress', function(event){
    
    if(event.key == 'Enter'){
        addTask()
    }
})



// function
function addTask(){
    const todoText = todoInp.value
    const li = document.createElement('li')
    const span = document.createElement('span')
    span.textContent = todoText
    li.append(span)
    todoList.appendChild(li)
    todoInp.value = '' // clear data
    // deletion-button
    const delBtn = document.createElement('button')
    delBtn.textContent = '❌'
    li.appendChild(delBtn)
    // deletion-task
    delBtn.addEventListener('click', function(){
        todoList.removeChild(delBtn.parentElement)
    
    })

    // completion-button
    const compBtn = document.createElement('button')
    compBtn.textContent = '✔️'
    li.appendChild(compBtn)
    // completion-task
    compBtn.addEventListener('click', function(){
        const parent = compBtn.parentElement
        
        const span = parent.querySelector('span')
        if(span.style.textDecoration === 'line-through'){
            span.style.textDecoration = 'none'
            span.style.color = 'black'
            compBtn.textContent = '✅'
        }
        else{
            span.style.textDecoration = 'line-through'
            span.style.color = 'grey'
            todoList.removeChild(parent) // removes and adds task to page only if its complete
            todoList.append(parent)
        }
    })


}