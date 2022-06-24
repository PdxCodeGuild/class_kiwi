// add items to a list
// be able to remove items
// mark the items as completed and have the text strikethrough

// global variables
const inputTodo = document.querySelector('#input')
const inputAdd = document.querySelector('#add')
const inputList = document.querySelector('#list')

inputAdd.addEventListener('click', addTask)

// task function
function addTask(){
    const textTodo = inputTodo.value
    const addedTask = document.createElement('li')
    const buttonSpan = document.createElement('span')
    buttonSpan.textContent = textTodo
    addedTask.append(buttonSpan)
    inputList.appendChild(addedTask)
    inputTodo.value = ''
    
    // complete button with strikethrough
    const completeButton = document.createElement('button')
    completeButton.textContent = 'Complete'
    addedTask.append(completeButton)

    // remove button that makes it disappear
    const removeButton = document.createElement('button')
    removeButton.textContent = 'Remove'
    addedTask.append(removeButton)
    removeButton.addEventListener('click', function(){
        inputList.removeChild(removeButton.parentElement)
    })
    
    completeButton.addEventListener('click', function(){
        const buttonParent = completeButton.parentElement
        const buttonSpan = buttonParent.querySelector('span')
        
        // create a function to determine if the text is complete
        if(buttonSpan.style.textDecoration === 'line-through'){
            buttonSpan.style.textDecoration = 'none'
        }

        else{
            buttonSpan.style.textDecoration = 'line-through'
            inputList.removeChild(buttonParent)
            inputList.append(buttonParent)
        }
    })
}