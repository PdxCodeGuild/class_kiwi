const computerChoiceDisplay = document.getElementById('computer-choice')
const playerChoiceDisplay = document.getElementById('player-choice')
const resultDisplay = document.getElementById('result')
const choices = document.querySelectorAll('button')
let playerChoice
let computerChoice

console.log(computerChoiceDisplay)
console.log(computerChoiceDisplay.id)
console.log(choices)
console.log(playerChoiceDisplay.innerHTML, 'before')

//listeners
choices.forEach(choice => choice.addEventListener('click', (e)=>{
    playerChoice = e.target.id
    playerChoiceDisplay.innerHTML = playerChoice

    console.log(playerChoiceDisplay.innerHTML, 'after')
}))

function createComputerChoice(){
    const weapons = ['rock', 'paper', 'scissors'];
    const random = Math.floor(Math.random() * weapons.length);
    computerChoiceDisplay.innerHTML = weapons[random];
}
