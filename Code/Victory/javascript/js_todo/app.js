// I used a variation of the class dtd 25Apr21 and code from below link
// https://github.com/bibeva/Javascript-Project-ToDo-List/blob/master/end/js/main.js ---

//Create a variable
const appBtn = document.querySelector('#app-btn')
const inputValue = document.querySelector('#input-val')
const appList = document.querySelector('#app-list')



//create Functions

function todoApp(){
    const todoText = inputValue.value

    const li = document.createElement('li')

        // Create a function that allows appending the list
    const span = document.createElement('span')
    span.textContent = todoText
    li.append(span)

    appList.appendChild(li)

        //create up
    const upBtn = document.createElement('button')
    upBtn.textContent = '⬆️'
    li.appendChild(upBtn)

        //Add a Listener
    upBtn.addEventListener('click', function(){
        let lasSib = li.previousElementSibling
        if (lasSib){
            appList.insertBefore(li, lasSib)
        }
    })

            // create down
    
    const downBtn = document.createElement('button')
    downBtn.textContent = '⬇️'
    li.appendChild(downBtn)

            //Add Listener
    
    downBtn.addEventListener('click', function(){
        let nexSib = li.nextElementSibling
        if (nexSib){
            appList.insertBefore(nexSib,li)
        }
    })

        //create delete
    const delBtn = document.createElement('button')
    delBtn.textContent = '🗑'
    li.append(delBtn)

        
    delBtn.addEventListener('click', function(){
    appList.removeChild(delBtn.parentElement)
        })

    const compBtn = document.createElement('button')
    compBtn.textContent = '✅'
    li.appendChild(compBtn)

        //AddListener
    compBtn.addEventListener('click', function(){
        const ulObject = compBtn.parentElement
        const span = ulObject.querySelector('span')
        if(span.style.textDecoration === 'line-through'){
            span.style.textDecoration = 'none'
            span.style.color = 'gray'
            appList.insertBefore(ulObject)
            compBtn.textContent = '✅'
        }
        else{
            span.style.textDecoration = 'line-through'
            span.style.color = 'gray'
        }
    })
}

//Create button/event listeners

appBtn.addEventListener('click', todoApp)

inputValue.addEventListener('keypress', function(event){
    if (event.key == 'Enter'){
        todoApp()
    }
})

