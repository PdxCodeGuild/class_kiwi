//selectors
const computerChoiceDisplay = document.getElementById('computer-choice')
const playerChoiceDisplay = document.getElementById('player-choice')
const resultDisplay = document.getElementById('result')
const choices = document.querySelectorAll('button')
let playerChoice
let computerChoice
let result

console.log(computerChoiceDisplay)
console.log(computerChoiceDisplay.id)
console.log(choices)



console.log(playerChoiceDisplay.innerHTML, 'before')
//listeners
choices.forEach(choice=>choice.addEventListener('click', (e) =>{
    playerChoice = e.target.id
    playerChoiceDisplay.innerHTML = playerChoice

    createComputerChoice()
    getResult()

    // console.log(playerChoiceDisplay, 'after')
}))

function createComputerChoice(){
    const randomNumber = Math.floor(Math.random() *choices.length) +1//3 +1
    console.log(randomNumber)

    if(randomNumber ===1){
        computerChoice = 'rock'
    }
    if(randomNumber ===2){
        computerChoice = 'scissors'
    }
    if(randomNumber === 3){
        computerChoice ='paper'
    }

    computerChoiceDisplay.innerHTML = computerChoice
}

function getResult() {
    if(computerChoice===playerChoice){
        result = 'We have a tie!'
    }
    if(computerChoice=== 'rock' && playerChoice ==='paper'){
        result = 'You won the game'
    }
    if(computerChoice=== 'rock' && playerChoice ==='scissors'){
        result = 'You lost the game'
    }
    if(computerChoice=== 'paper' && playerChoice ==='scissors'){
        result = 'You won the game'
    }
    if(computerChoice=== 'paper' && playerChoice ==='rock'){
        result = 'You lost the game'
    }
    if(computerChoice=== 'scissors' && playerChoice ==='rock'){
        result = 'You won the game'
    }
    if(computerChoice=== 'scissors' && playerChoice ==='paper'){
        result = 'You lost the game'
    }
    resultDisplay.innerHTML = result

}


























































// function getResult() {
//     if(computerChoice===playerChoice){
//         result = 'We have a tie!'
//     }
//     if(computerChoice=== 'rock' && playerChoice ==='paper'){
//         result = 'You won the game'
//     }
//     if(computerChoice=== 'rock' && playerChoice ==='scissors'){
//         result = 'You lost the game'
//     }
//     if(computerChoice=== 'paper' && playerChoice ==='scissors'){
//         result = 'You won the game'
//     }
//     if(computerChoice=== 'paper' && playerChoice ==='rock'){
//         result = 'You lost the game'
//     }
//     if(computerChoice=== 'scissors' && playerChoice ==='rock'){
//         result = 'You won the game'
//     }
//     if(computerChoice=== 'scissors' && playerChoice ==='paper'){
//         result = 'You lost the game'
//     }
//     resultDisplay.innerHTML = result
// 