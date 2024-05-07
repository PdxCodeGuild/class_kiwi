// Approach A

// needs timing in nano? seconds: 2000 is 2 seconds
setTimeout(logMessage, 2000)
function logMessage(){
    // console.log('You get a Car!')
}

// Approach B
setTimeout(function(){
    // console.log('Damn... You didnt win a car')
}, 4000)

// ---------------------------

// let counter= 0
// // 500 = half a second
// setInterval(changeTime, 500)

// function changeTime(){
//     counter ++ //+= 1 
//     // console.log(counter)
// }

// increment "seconds" by every 'second'

let seconds=0

// let counter= setInterval(function(){
//     //selector
//     const currentCount=document.querySelector('.count')
//     seconds ++ 
//     currentCount.textContent = seconds
// }, 1000)

let counter
const startButton= document.querySelector('.start-btn')
startButton.addEventListener('click',function(){
    counter= setInterval(function(){
        const currentCount= document.querySelector('.count')
        seconds ++
        currentCount.textContent= seconds
    }, 1000)
})

// selector
const stopButton= document.querySelector('.stop-btn')
// listener
stopButton.addEventListener('click',function(){
    clearInterval(counter)
})