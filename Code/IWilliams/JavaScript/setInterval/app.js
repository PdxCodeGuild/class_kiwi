//Approach A
// setTimeout(logMessage, 2000)
// function logMessage(){
//     console.log('You Get A Car!')
// }

// //ApproachB
// setTimeout(function(){
//     console.log('Ooops....My Bad. No car for you')
// }, 4000)

// let counter =0
// setInterval(changeTime, 500)

// function changeTime(){
//     counter +=1 //++
//     console.log(counter)
// }

//increment seconds by every second
let seconds = 0

let counter
const startButton = document.querySelector('.start-btn')
startButton.addEventListener('click', function(){
    counter =setInterval(function(){
        const currentCount = document.querySelector('.count')
        seconds ++
        currentCount.textContent = seconds
    } ,1000)

})


// let counter = setInterval(function(){
//     //selector
//     const currentCount = document.querySelector('.count')
//     seconds +=1
//     currentCount.textContent = seconds
// }, 1000)

//selector
const stopButton = document.querySelector('.stop-btn')
stopButton.addEventListener('click', function(){
    clearInterval(counter)
})