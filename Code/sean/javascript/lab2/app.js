let body = document.body
let input = document.querySelector('#input')
let button = document.querySelector('#button')
let ul = document.querySelector('#ul')


button.addEventListener('click', function(e) {
    e.preventDefault
    let newLi = document.createElement('li')
    todo = input.value
    newLi.innerText = `${todo}`
    let deletebtn = document.createElement('button')
    deletebtn.innerText = 'delete'
    deletebtn.addEventListener('click', function(e){
        ul.removeChild(newLi)
    })
    let completedbtn = document.createElement('button')
    completedbtn.innerText = 'Complete'
    completedbtn.addEventListener('click', function(e){
        newLi.style.textDecoration = 'line-through'
    })
    newLi.append(deletebtn)
    newLi.append(completedbtn)
    ul.append(newLi)
    input.value = ""
})