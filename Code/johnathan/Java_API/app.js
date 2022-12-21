//console log fetech request
//console.log(fetch('http://jsonplaceholder.typicode.com/posts/1'))

//console log the response 
// // step 1
// fetch('http://jsonplaceholder.typicode.com/posts/1')// actual request -- manage promise 
// .then(function(response){
//     console.log(response)
// })

// fetch request returns successful data chain on the then method
// Promise() --> pending, accepted, rejected 
// .then() --> successful/accepted 
//.catch() --> error/rejected 

// step 2
// fetch('http://jsonplaceholder.typicode.com/posts/1')// actual request 
// .then(function(response){
//     // console.log(response)
//     return response.json()// converted to json object -- format that javascript can work with: // key/value ---? 
// })
// .then(function(data){
//     console.log(data)
//     console.log(data.title)
//     console.log(data.id)
// })



// // ************** POST REQUEST */
// const blogPost ={
//     title: "Kiwi Post", 
//     body: "Class Kiwi 2022",
//     UserId: 1
// }

// fetch('http://jsonplaceholder.typicode.com/posts/1', {
//     method: "POST", 
//     header: {
//         "Content-Type": "application/json"
//     },
//     body: JSON.stringify(blogPost)
// }) 
// .then(function(response){
//     return response.json() 
// })
// .then(function(data){
//     console.log(data)
    
// })

// //manage bad request to api 
// fetch('http://jsonplaceholder.typicode.com/posts/1')
// .then(function(response){ //response.ok // 200 - 299 range 
//     if(!response.ok)
//     return new Error ('Bad Requests')
//     return new Error(response.status)
// })
// .then(function(data){
//     console.log(data)
// })
// .catch(function(error){
//     console.log(error.error)
// })

// //pending, accept, reject




// Approach A
setTimeout(logmessage, 2000)
function logmessage(){
    console.log('You Get a Car!')
}

// Approach B
setTimeout(function(){})


let couinter = 0
setInterval(changeTime, 500)

function changeTime(){
    counter +=1 //++
    console.log(counter)
}

//increment seconds by every second 
let seconds = 0
setInterval(function(){
    //selector 
    const currentCount
})