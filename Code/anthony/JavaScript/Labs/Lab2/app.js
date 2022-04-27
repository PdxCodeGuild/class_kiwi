const todoBox = document.querySelector('#todo-box')
const todoButton = document.querySelector('#todo-button')
const todoList = document.querySelector('#todo-list')

//Listeners
todoButton.addEventListener('click', btnClick)
todoBox.addEventListener('keypress',function(event){
  if(event.key === 'Enter'){
    btnClick()
  }
})




//functions
function btnClick(){
  //list values submitted from input 
  const text = todoBox.value
  const li = document.createElement('li')

  li.textContent = text
  todoList.appendChild(li)
  todoBox.value = ''

  //DELETE BUTTON
  const delBtn = document.createElement('button')
  delBtn.textContent= '❌'
  li.append(delBtn)

  //checkmark
  const check =document.createElement('button')
  check.textContent='✅'
  li.append(check)

  //events for delete button and checkmark
  delBtn.addEventListener('click', function(){
    todoList.removeChild(delBtn.parentElement)
  })


  //mark item as completed
 check.addEventListener('click', function(){

  const parent = check.parentElement
  
  // const span = parent.querySelector('span')
  if(li.style.textDecoration === 'line-through'){
    li.style.textDecoration = 'none'
    li.style.color = 'black'
    todoList.insertBefore(parent, todoList.firstChild)
    completeBtn.textContent='✔'
  }else{
    li.style.textDecoration === 'line-through'
    li.style.color = 'green'
    todoList.removeChild(parent)//remove item from page
  todoList.append(parent)//add it back to bottom of list
  }
})

}