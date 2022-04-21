
// const headers= document.getElementsByTagName('h2')
// console.log(headers)
// console.log(headers[0])

// const list= document.getElementsByClassName('item')
// console.log(list)

// const button= document.getElementById('submit')
// console.log(button)

// calling all h2 elements within index.html
// const headers= document.querySelectorAll('h2')
// const headers= document.querySelector('h2') // returns the first occurrence of object
// console.log(headers)

// calling class="item"
// const list= document.querySelectorAll('.item')
// console.log(list)

// targets 'a' tag within id="list"
// const thing= document.querySelector('#list a')
// console.log(thing)

//---------------------------------------------------------------

// selector
// const button= document.querySelector('#submit')

// listeners
// calling anonymous function within event listener
// button.addEventListener('click', function(){
    // console.log('testing')
// })


// button.addEventListener('click',addItem)

// 'hoist' functions to the top of the page down. // Make and Call function at anywhere on the page 

// function addItem(){
//     console.log('test button')
// }

//---------------------------------------------------------------

// Parent
const list= document.querySelector('#list') // parent
// Child
const items= list.children // Selecting the children of the list object
// targeting <b> tag inside 'num' class
const num= document.querySelector(".num b")
// 


const button= document.querySelector('#submit')

button.addEventListener('click',function(){
    // Creating newItem: <li></li>
    const newItem= document.createElement('li')
    // adding class="item" to newItem: <li></li> 
    newItem.classList.add('item')
    // adding text to the inside of the new li tag
    newItem.innerText= `item ${items.length + 1}` 
    // append child
    list.appendChild(newItem)
    // count
    num.innerText= items.length

})
// Selector
const mainTitle= document.querySelector('.main-title')
// listener
const colorChange= document.querySelector('.color')
colorChange.addEventListener('click',function(){
    if(mainTitle.style.color == 'black'){
        mainTitle.style.color = 'blue'
    }
    else{
        mainTitle.style.color = 'black'
    }
})

const test= document.querySelector('.thing')
const testButton= document.querySelector('.css')
testButton.addEventListener('click',function(){
    // test.classList.add('test')
    if (test.style.color == 'black') {
        test.classList.add('test')
    }
})