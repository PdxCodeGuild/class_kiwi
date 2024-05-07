
const button= document.querySelector('#submit') // line:25
const list= document.querySelector('#list') //
// const items= list.children // line:30
const num= document.querySelector('.num b') // line:35
const nameInput= document.querySelector('.name-input') // line:31
// Creating newItem: <li></li>
const newItem= document.createElement('li') // line:28
// Selector
const mainTitle= document.querySelector('.main-title') // line:15
// listener
const colorChangeButton= document.querySelector('.color')
// Changing the color of main
colorChangeButton.addEventListener('click',function(){
    if(mainTitle.style.color == 'black'){
        mainTitle.style.color = 'blue'
    }
    else{
        mainTitle.style.color = 'black'
    }
})

// ------------------------------------------------------

button.addEventListener('click',function(e){
    // prevents the form from reloading page
    e.preventDefault()
    newItem.classList.add('item')  // adding class="item" to newItem: <li></li> 
   
    // newItem.innerText= `item ${items.length + 1}` // adding text to the inside of the new li tag
    newItem.innerText= nameInput.value
    nameInput.value= ""

    list.appendChild(newItem) // append child
    num.innerText= items.length // Item count

    //add the event listener
    newItem.addEventListener('click',deleteItem)
})

list.addEventListener('click',function(){
    list.classList.toggle('fade')
})
//event object? (e)

// delete 
function deleteItem(e){
    // console.log(e)
    // console.log(e.target)

    // allows you to click on the item without trigging line 29
    e.stopPropagation()
    e.target.remove()
}   


