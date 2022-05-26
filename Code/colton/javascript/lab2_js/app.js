

const button = document.querySelector('.submit')
const todoList = document.querySelector('.todo-list')
const items = todoList.children
const itemInput = document.querySelector('#additem')



button.addEventListener('click', function(){    

    const newItem = document.createElement('li')
    newItem.classList.add('item')
    newItem.innerHTML = `${itemInput.value}`
    todoList.appendChild(newItem)
    
    let removeTask = document.createElement('input')
    removeTask.setAttribute('type', 'button')
    removeTask.setAttribute("value", "Remove")
    removeTask.setAttribute("id", "removeButton")
    newItem.appendChild(removeTask)

    removeTask.addEventListener('click', function(e) {
        e.stopPropagation()
        newItem.parentNode.removeChild(newItem)
    })

    newItem.addEventListener('click', function(e){
        e.stopPropagation()
        newItem.style = 'text-decoration: line-through;'

    })

    itemInput.value = ''


})

itemInput.addEventListener('keypress', function(e){    
    if(e.key === 'Enter'){
    const newItem = document.createElement('li')
    newItem.classList.add('item')
    newItem.innerText = `${itemInput.value}`
    todoList.appendChild(newItem)
    
    let removeTask = document.createElement('input')
    removeTask.setAttribute('type', 'button')
    removeTask.setAttribute("value", "Remove")
    removeTask.setAttribute("id", "removeButton")
    newItem.appendChild(removeTask)

    removeTask.addEventListener('click', function(e) {
        e.stopPropagation()
        newItem.parentNode.removeChild(newItem)
    })

    newItem.addEventListener('click', function(e){
        e.stopPropagation()
        newItem.style = 'text-decoration: line-through;'

    })
    itemInput.value = ''
    }
    
})
