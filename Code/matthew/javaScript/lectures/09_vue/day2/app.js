
const app= new Vue({
    //el = element
    el: '#app',
    data :{
        headerText: 'Vue to do',
        completeTodo: [],
        incompleteTodo:[],
        newTodoText: '',
        idCount: 1,
    },  
        methods:{
            addTodo: function(){
                this.incompleteTodo= this.incompleteTodo.concat({
                    id: this.idCount,
                    text: this.newTodoText,
                    complete: false
                })
                this.idCount ++
                this.newTodoText= ''
            },
            // toggle complete value
            
            completeToggle: function(todoId){
                // combine the completed and incomplete 
                let todos= this.completeTodo.concat(this.incompleteTodo)
                
                // change the selected todo items value
                                //x      //x.id      // if todoId = todo.id {}       
                //if they do not match do nothing //if they do match, {...(copy), flip boolean value}
                                    //todo.id not= todoId ?ifTrue doNothing:{-else- ... copyItem, complete: flipValue}
                todos= todos.map((todo)=>todo.id != todoId ? todo: {... todo, complete:!todo.complete })

                // split todos into separate arrays
                                                // filtering complete=true
                this.completeTodo= todos.filter(todo=>todo.complete)
                                                // compete=false
                this.incompleteTodo= todos.filter(todo=>!todo.complete)
            },
            deleteTodo: function(todoId){
                let todos= this.completeTodo.concat(this.incompleteTodo)
                
                // loop thru todos, keep todo that does not match TodoId

                //deletes the todo, filters through the array setting up for line 48 and 49
                todos= todos.filter(todo=>todo.id !== todoId)

                this.completeTodo= todos.filter(todo=>todo.complete)
                this.incompleteTodo= todos.filter(todo=>!todo.complete)

            }
    }
})