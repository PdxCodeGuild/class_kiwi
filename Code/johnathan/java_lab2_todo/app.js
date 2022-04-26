//selectors 

let addTodoBtn = document.getElementById('addTodo');
let TodoContainer = document.getElementById('TodoContainer');
let inputField = document.getElementById('inputField');


//listeners
addTodoBtn.addEventListener('click', addTodo) 
inputField.addEventListener('keypress', function(e){
    if(e.key === 'Enter'){ addTodo()}
})
//  Add an item to the list -- function addTodo
function addTodo(){
    var paragraph = document.createElement('p'); 
    paragraph.classList.add('paragraph-styling'); //add styling 
    paragraph.innerText = inputField.value; 
    TodoContainer.appendChild(paragraph); // append paragraph to todo container
    inputField.value = "";

    //create delete button, text = 'X'
    const delBtn = document.createElement('button')
    delBtn.textContent = 'X'
    paragraph.append(delBtn)

    //b. Remove an item from the list -- delete todo
    delBtn.addEventListener('click', function(){
            paragraph.removeChild(delBtn.parentElement) // remove button from parent

    })

    //c. Mark as complete 
    paragraph.addEventListener('dblclick', function(){
        paragraph.style.textDecoration = "line-through";
    })
}