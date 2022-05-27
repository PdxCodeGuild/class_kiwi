{/* <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.27.2/axios.min.js" integrity="sha512-odNmoc1XJy5x1TMVMdC7EMs3IVdItLPlCeL5vSUPN2llYKMJ2eByTTAIiiuqLg+GdNr9hF6z81p27DArRFKT7A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script> */}
const BASE_URL= 'http://127.0.0.1:8000/'

const csrfToken= document.getElementsByName('csrfmiddlewaretoken')[0]
 
axios.defaults.xsrfHeaderName= 'X-CSRFToken'
axios.defaults.headers ={
    'Content-Type': 'application/json',
    'X-CSRFToken':csrfToken.value, // including django csrf token
}

const app= new Vue({
    // to remove syntax errors with django 
    delimiters: ['[[', ']]'],
    //el = element
    el: '#app',
    data :{
        headerText: 'Vue to do',
        completeTodo: [],
        incompleteTodo:[],
        newTodoText: '',
        idCount: 1,
    },  
        // created: life cycle hook
        created: function(){
            axios({
                url: BASE_URL + 'list/',
                method: 'GET'
            })
            //.then(response=>console.log(response))
            .then(response =>{
                // pull data from django server to page
                this.updateTodos(response.data.todos)
            })
            .catch(error=>console.log(error))
            
        },
        methods:{
            //create method that toggles complete and delete methods
            updateTodos: function(todos){
                this.completeTodo= todos.filter(todo=>todo.completed)
                this.incompleteTodo= todos.filter(todo=>!todo.completed)
            },

            // addTodo: function(){
            //     this.incompleteTodo= this.incompleteTodo.concat({
            //         id: this.idCount,
            //         text: this.newTodoText,
            //         complete: false
            //     })
            //     this.idCount ++
            //     this.newTodoText= ''
            // },
            addTodo: function(){
                axios({
                    url: BASE_URL + "create/",
                    method: "POST",
                    data: {
                        'new_todo_text' : this.newTodoText
                    }
                })
                // .then(response=>console.log(response))
                .then(response=>{
                    this.updateTodos(response.data.todos)
                })
                .catch(error=>console.log(error.response))
            },

            // toggle complete value
            
            // completeToggle: function(todoId){
            //     // combine the completed and incomplete 
            //     let todos= this.completeTodo.concat(this.incompleteTodo)
                
            //     // change the selected todo items value
            //                     //x      //x.id      // if todoId = todo.id {}       
            //     //if they do not match do nothing //if they do match, {...(copy), flip boolean value}
            //                         //todo.id not= todoId ?ifTrue doNothing:{-else- ... copyItem, complete: flipValue}
            //     todos= todos.map((todo)=>todo.id != todoId ? todo: {... todo, complete:!todo.complete })
            //     this.updateTodos(todos)
            //     // split todos into separate arrays
            //                                     // filtering complete=true
            //     // this.completeTodo= todos.filter(todo=>todo.complete)
            //                                     // compete=false
            //     // this.incompleteTodo= todos.filter(todo=>!todo.complete)

            completeToggle: function(todoId){
                axios({
                    url: BASE_URL + `toggle-complete/${todoId}`,
                    method: "POST",

                })
                // .then(response=>{console.log(response.data)})
                .then(response=>{
                    this.updateTodos(response.data.todos)
                })
                .catch(error=>console.log(error))
            },

            // deleteTodo: function(todoId){
            //     let todos= this.completeTodo.concat(this.incompleteTodo)
                
            //     // loop thru todos, keep todo that does not match TodoId

            //     //deletes the todo, filters through the array setting up for line 48 and 49
            //     todos= todos.filter(todo=>todo.id !== todoId)
            //     this.updateTodos(todos)
            //     // this.completeTodo= todos.filter(todo=>todo.complete)
            //     // this.incompleteTodo= todos.filter(todo=>!todo.complete)

            // }b
            deleteTodo: function(todoId){
                axios({
                    url: BASE_URL + `delete/${todoId}`,
                    method: "post"
                })
                .then(response=>{
                    this.updateTodos(response.data.todos)
                })
                .catch(error=>console.log(error))
            }
    }
})