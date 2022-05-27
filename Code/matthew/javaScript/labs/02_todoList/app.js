//
const newItem= document.querySelector('#new-item')
const newBtn= document.querySelector('#new-btn')
const list= document.querySelector('#list')

//
newBtn.addEventListener('click', addItem)

newItem.addEventListener('keypress',function(e){
    // console.log(e)
    if(e.key=== 'Enter'){
        addItem()
    }
})

function addItem(){
    const itemText= newItem.value
    // reset input field
    newItem.value = ''

    const li= document.createElement('li')
    const span= document.createElement('span')
    span.textContent= itemText
    li.append(span)
    list.appendChild(li)

// complete
    const complete= document.createElement('input')
    complete.setAttribute('type','checkbox')
    li.append(complete)
    complete.addEventListener('click',function(){
        const parent= complete.parentElement
        const span = parent.querySelector('span')

        if(complete.checked === true ){
            span.style.textDecoration= 'line-through'
            span.style.color= 'grey'
            list.removeChild(parent)
            list.append(parent)
        }
        else{
            list.insertBefore(parent, list.firstChild)
            span.style.textDecoration= 'none'
            span.style.color= 'black'
        }
    })

// delete
    const delBtn= document.createElement('button')
    delBtn.textContent= '❌'
    li.append(delBtn)

    delBtn.addEventListener('click',function(){
    list.removeChild(delBtn.parentElement)
    })

}