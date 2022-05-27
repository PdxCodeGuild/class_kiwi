// selectors
const inputTodo = document.querySelector('#input-todo')
const inputAdd = document.querySelector('#add-todo')
const inputList = document.querySelector('#list-todo')


// console.log(inputTodo.value)

// listeners

inputAdd.addEventListener('click', addTask) // ADD TASK

function addTask(){
    const textTodo = inputTodo.value
    const addedTask = document.createElement('li')
    const btnSpan = document.createElement('span')
    btnSpan.textContent = textTodo
    addedTask.append(btnSpan)
    inputList.appendChild(addedTask)
    inputTodo.value = ''
    
    // delete-button
    const delBtn = document.createElement('button')
    delBtn.textContent = '❌'
    addedTask.append(delBtn)
    delBtn.addEventListener('click', function(){
        inputList.removeChild(delBtn.parentElement)
    })
    

    // completed-button
    const compBtn = document.createElement('button')
    compBtn.textContent = '✔️'
    addedTask.append(compBtn)

    // ------------------

    compBtn.addEventListener('click', function(){
        const btnParent = compBtn.parentElement
        const btnSpan = btnParent.querySelector('span')
        

        if(btnSpan.style.textDecoration === 'line-through'){
            btnSpan.style.textDecoration = 'none'
            btnSpan.style.color = 'black'
            
        }
        else{
            btnSpan.style.textDecoration = 'line-through'
            btnSpan.style.color = 'grey'
            inputList.removeChild(btnParent)
            inputList.append(btnParent)
        }
    })
}