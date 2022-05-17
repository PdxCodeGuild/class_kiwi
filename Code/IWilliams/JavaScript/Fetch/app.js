//console log fetch request
// console.log(fetch('http://jsonplaceholder.typicode.com/posts/1'))

//Promise() --> pending, accepted,rejected
//.then() --> successful/accepted
//.catch() --> error/rejected 


//console log the response
// fetch('http://jsonplaceholder.typicode.com/posts/1')//actual request
// .then(function(response){
//     console.log(response)
// })


//make a POST request
// const blogPost = {
//     title: "Kiwi post",
//     body: "Class Kiwi 2022",
//     userId: 1
// }
// fetch('http://jsonplaceholder.typicode.com/posts', {
//     method: "POST",
//     headers:{
//         "Content-Type": "application/json"
//     },
//     body: JSON.stringify(blogPost)
// })//actual request
// .then(function(response){
//     //console.log(response)
//     return response.json() 
// })
// .then(function(data){
//     console.log(data)
// })

//manage bad request to api
fetch('http://jsonplaceholder.typicode.com/poss/1')//actual request
.then(function(response){  //response.ok //200 -299range 
    if(!response.ok){

        //return new Error('Bad Requests ssss')
        return new Error(response.status)
    }
})
.then(function(data){
    console.log(data)
})
// .catch(function(error){
//    console.log(error.error)
// })



//pending, accept, reject