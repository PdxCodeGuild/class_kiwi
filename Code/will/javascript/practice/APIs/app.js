// ************* FETCH REQUEST **************
// console.log(fetch('http://jsonplaceholder.typicode.com/posts/1'))

// fetch('http://jsonplaceholder.typicode.com/posts/1')
// .then(function(response){
//     return response.json
// })
// .then(function(data){
//     console.log(data)
//     console.log(data.title)
//     console.log(data.id)
// })


// ********** POST REQUEST ************
// const blogPost = {
//     title: "Kiwi Post",
//     body: "Class Kiwi 2022",
//     userId: 1
// }

// fetch('http://jsonplaceholder.typicode.com/posts', {
//     method: "POST",
//     headers: {"Content-Type": "application/json"},
//     body: JSON.stringify(blogPost)
// })
// .then(function(response){
//     return response.json()
// })
// .then(function(data){
//     console.log(data)
// })

fetch('http://jsonplaceholder.typicode.com/postss/1')
.then(function(response){
    if(!response.ok)
    return new Error('Bad Requests ')
})
.then(function(data){
    console.log(data)
})

