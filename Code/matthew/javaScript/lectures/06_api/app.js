

// console.log(fetch("http://jsonplaceholder.typicode.com/posts/1")) // returns promise
// promise --> pending


// Promise --> pending, accepted, rejected
// .then() --> successful/accepted
// .catch() --> unsuccessful/error/rejected
// .finally() -->

// fetch request ---------

// fetch data
// fetch("http://jsonplaceholder.typicode.com/posts/1")
// .then(function(response){
//     // console.log(response)
// // convert the response data to JSON
//     return response.json() 
// })
// .then(function(data){
//     console.log(data)
//     console.log(data.id, data.body)
// })


// POST request ---------


// const blogPost = {
//     title: 'Kiwi Post',
//     body: 'Class Kiwi',
//     userId: 1
// }

// fetch("http://jsonplaceholder.typicode.com/posts", {
//     method: "POST",
//     // MUST be headers with the s 
//     headers: {
//         'Content-Type':'application/json'
//     },
//     body: JSON.stringify(blogPost)
// })
// // for every promise you need a "then"
// .then(function(response){
// // convert the response data to JSON
//     // console.log(response.json())
//     return response.json() 
// })
// // for every promise you need a "then"
// .then(function(data){
//     // display the actual data
//     console.log(data)
//     console.log(data.id, data.body)
// })

// ----------------

// managing bad request to api
fetch("http://jsonplaceholder.typicode.com/poss/1") // populate 404 error
.then(function(response){ // response.ok // 200-299 rng
    // if not response.ok
    if(!response.ok){
        return new Error('Bad Request n stuff',)
        // return new Error(response.status)
    }
    return response.json()
})
.then(function(data){
    console.log(data)
})
// catching the rejected promise // ???
// .catch(function(e){ // ?????
//     console.log(e.error) // ????
// }) // ???
// .catch(function(error){ // ????
//     console.log(error.error) // ???
// }) // ??


// Promise = --> pending, accepted, rejected

