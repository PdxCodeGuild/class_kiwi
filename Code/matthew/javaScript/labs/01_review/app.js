// selectors
const computerChoiceDisplay = document.getElementById('computer-choice')
const playerChoiceDisplay= document.getElementById('player-choice')
const resultDisplay= document.getElementById('result')
const choices= document.querySelectorAll('button')
// global variable
let playerChoice
let computerChoice
let result

// console.log(computerChoiceDisplay)
// console.log(playerChoiceDisplay)
// console.log(resultDisplay)
// console.log(choices)


//listeners

                // arrow function  //event               //e or event
choices.forEach(choice =>choice.addEventListener('click', (e)=>{
    //update global variable
    // ? target.id ?
    playerChoice= e.target.id // e.target.id is calling id on choices -> choice variable
    playerChoiceDisplay.innerHTML=playerChoice
    console.log(playerChoiceDisplay, 'after')
    createComputerChoice()
    getResult()
}))

function createComputerChoice(){
                        //random number between 0 and .99
    const randomNumber= Math.floor(Math.random() * choices.length)  // 3 + 1
    // console.log(randomNumber)
    if(randomNumber === 0){
        computerChoice = 'rock'
    }
    if(randomNumber === 1){
        computerChoice = 'scissors'
    }
    if(randomNumber === 2){
        computerChoice = 'paper'
    }
    console.log(computerChoice)
    computerChoiceDisplay.innerText = computerChoice

}
function getResult(){
    if(computerChoice == playerChoice ){
        result = 'Tie'
    }
    if(computerChoice == 'rock' && playerChoice == 'paper'){
        result = 'You win'
    }
    if(computerChoice == 'rock' && playerChoice == 'scissors'){
        result = 'You Loose'
    }
    if(computerChoice == 'scissors' && playerChoice == 'rock'){
        result = 'You win'
    }
    if(computerChoice == 'scissors' && playerChoice == 'paper'){
        result = 'You Loose'
    }
    if(computerChoice == 'paper' && playerChoice == 'scissors'){
        result = 'You win'
    }
    if(computerChoice == 'paper' && playerChoice == 'rock'){
        result = 'You Loose'
    }
    // 
    resultDisplay.innerHTML = result
}



// from joesph
// function createComputerChoice(){
//     const weapons = ['rock', 'paper', 'scissors'];
//     const random = Math.floor(Math.random() * weapons.length);
//     return(weapons[random]);
// };