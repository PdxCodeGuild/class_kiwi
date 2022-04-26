//selectors
const todoBtn = document.querySelector('#todo-btn')
const todoInput = document.querySelector('#todo-input')
const todoList = document.querySelector('#todo-list')

//listeners
todoBtn.addEventListener('click', addTodo)
todoInput.addEventListener('keypress', function(e){
  if(e.key === 'Enter'){
    addTodo()
  }
})

function addTodo() {
  const todoText = todoInput.value 
  const li = document.createElement('li')
  li.className = 'list-group-item';

  //create empty span
  const span = document.createElement('span')
  span.textContent = todoText
  li.append(span)

  todoList.appendChild(li)
  todoInput.value = ''  //clear input

  //complete button
  const completeBtn = document.createElement('button')
  completeBtn.className = 'btn btn-outline-success btn-sm float-start me-2';
  completeBtn.textContent = '✓'
  li.appendChild(completeBtn)

  //create delete button
  const delBtn = document.createElement('button')
  delBtn.className = 'btn btn-outline-danger btn-sm float-end';
  delBtn.textContent = '✕'
  li.append(delBtn)

  //add delete event listener
  delBtn.addEventListener('click', function(){
    todoList.removeChild(delBtn.parentElement)
  })

  // move the checked todo to bottom of list
  completeBtn.addEventListener('click', function(){
    const parent = completeBtn.parentElement
    const span = parent.querySelector('span')
    if (span.style.textDecoration === 'line-through') {
      span.style.textDecoration = 'none'
      span.style.color = 'black'
      todoList.insertBefore(parent, todoList.firstChild)
      completeBtn.className = 'btn btn-outline-success btn-sm float-start me-2';
      completeBtn.textContent = '✓'
    } else {
      span.style.textDecoration = 'line-through'
      span.style.color = 'gray'
      completeBtn.className = 'btn btn-outline-secondary btn-sm float-start me-2';
      todoList.removeChild(parent) //remove item from page
      todoList.append(parent) // add item back
    }
  })

}