// const headers = document.getElementsByTagName('h2')
// const list = document.getElementsByClassName('item')
// const button = document.getElementById('submit')

//const headers = document.querySelector('h2')
// const headers = document.querySelector('h2')
// const list = document.querySelectorAll('.item') 
// const list = document.querySelector('#list a')
// console.log(list)


//selector
// const button = document.querySelector('#submit')

// //listeners 
// button.addEventListener('click', function(){
//     console.log('Add something')
// })

// // button.addEventListener('click', addItem)

// // function addItem(){
// //     console.log("Test Buttonzzzzzz")
// // }

//selectors
// const button = document.querySelector('#submit')
// const todoList = document.querySelector("#todo-list") //select parent
// const items = todoList.children //selects children of parent (lis)
// const todoNum = document.querySelector('.todo-num b')
// //console.log(todoNum)


// button.addEventListener('click', function(){
//     const newItem = document.createElement('li')
//     newItem.classList.add('item')
//    // newItem.innerText = "Item 3"
//    newItem.innerText = `Item ${items.length +1}`
    
//     todoList.appendChild(newItem)
//     todoNum.innerText = items.length

//     //console.log(newItem)
// })

// //Number of items -...whatever 

// //selector
// const mainTitle = document.querySelector('.main-title')

// //listener
// button.addEventListener('click', function(){
//     // mainTitle.style.color = 'blue'
//     // mainTitle.style.fontSize = '2.5rem' 

//     mainTitle.classList.add('new-style')

// })
/////******************DOM Day 2************************** */
const button = document.querySelector('#submit')
const todoList = document.querySelector("#todo-list") //select parent
const items = todoList.children //selects children of parent (lis)
const todoNum = document.querySelector('.todo-num b')
const mainTitle = document.querySelector('main-title')
const nameInput = document.querySelector('.name-input')

button.addEventListener('click', function(e){
    e.preventDefault()
    const newItem = document.createElement('li')
    newItem.classList.add('item')
   // newItem.innerText = "Item 3"
   //newItem.innerText = `Item ${items.length +1}`
   newItem.innerText = nameInput.value
   //console.log(newItem)
    
    todoList.appendChild(newItem)
    todoNum.innerText = items.length
    nameInput.value = ''
    //add the event listener to element
    newItem.addEventListener('click', deleteItem)
})

// for(item of items) {
//     item.addEventListener('click', deleteItem)
// }

todoList.addEventListener('click', function(e){
    todoList.classList.toggle('fade')
})



function deleteItem(e) {
    // console.log(e) 
    // console.log(e.target)
    e.stopPropagation()
    e.target.remove() 

}




