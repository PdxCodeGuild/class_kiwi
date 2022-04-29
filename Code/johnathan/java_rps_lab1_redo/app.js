const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('uesr-choice')
const resultDisplay = document.getElementById('result')
const possibleChoices = document.querySelector('button')
let userChoice

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e)=> {
    userChoice = e.target.id
    userChoiceDisplay.innerHTML = userChoice
    generateComputerChoice()
    getResult()

}))
// generate random number 
function generateComputerChoice(){
    const randomNumber = Math.floor(Math.random() * 3) + 1

    if (randomNumber === 1){
        computerChoice = 'rock'
    }
    if (randomNumber === 2){
        computerChoice = 'paper'
    }
    if (randomNumber === 3){
        computerChoice = 'scissors'
    }
    computerChoiceDisplay.innerHTML = computerChoice
}

// function to retrieve results
function getResult(){
    if (computerChoice === userChoice){
        result = 'its a draw!'
    }
    if (computerChoice === 'rock' && userChoice === 'paper'){
        result = 'you win!'
    }
    if (computerChoice === 'paper' && userChoice === 'rock'){
        result = 'you lost!'
    }
    if (computerChoice === 'scissors' && userChoice === 'paper'){
        result = 'you lose!'
    }
    if (computerChoice === 'scissors' && userChoice === 'rock'){
        result = 'you win!'
    }
    if (computerChoice === 'paper' && userChoice === 'scissors'){
        result = 'you win!'
    }
    if (computerChoice === 'paper' && userChoice === 'rock'){
        result = 'you lost!'
    }
}