
// selectors
let userChoice = prompt('Rock paper scissors').toLocaleLowerCase()
        // Random Computer Choice logic
let computerChoice = {1:'rock', 2:'paper', 3:'scissors'}
let randomNumber = Math.floor(Math.random()*3)+1
let randomComputer = computerChoice[randomNumber]
        // Random Computer Choice logic
let output = document.querySelector('.output')
let computerSelect = document.querySelector('#computer-selection b')
let userSelect = document.querySelector('#user-selection b')


// listeners
computerSelect.innerText = computerChoice[randomNumber]
userSelect.innerText = userChoice


// USER CHOSE ROCK
if (userChoice === 'rock'){
    if(computerChoice[randomNumber] === 'scissors'){
        output.innerText = 'You WIN!'
    }
    else if(computerChoice[randomNumber] === 'paper'){
        output.innerText = 'You LOSE.'
    }
    else{
        output.innerText = 'It is a TIE.'
    }
}

// USER CHOSE PAPER
else if (userChoice === 'paper'){
    if(computerChoice[randomNumber] === 'scissors'){
        output.innerText = 'You LOSE.'
    }
    else if(computerChoice[randomNumber] === 'paper'){
        output.innerText = 'It is a TIE.'
    }
    else{
        output.innerText = 'You WIN!'
    }
}

// USER CHOSE SCISSORS
else if (userChoice === 'scissors'){
    if(computerChoice[randomNumber] === 'scissors'){
        output.innerText = 'It is a TIE.'
    }
    else if(computerChoice[randomNumber] === 'paper'){
        output.innerText = 'You WIN!'
    }
    else{
        output.innerText = 'You LOSE.'
    }
}

// USER CHOSE NOT ALLOWED
else{
    output.innerText = 'You did not enter a valid choice'
    computerSelect.innerText = ''
    userSelect.innerText = ''
}