const button = document.querySelector('#submit')
const choiceInput = document.querySelector('.choice-input')
var compChoices = ["rock", "paper", "scissors"]


button.addEventListener('click', function(e){
    e.preventDefault()
    const compSelect = compChoices[(Math.random() * compChoices.length) | 0]
    playerChoice = choiceInput.value
    playerChoice = playerChoice.toLowerCase()
    console.log(playerChoice)
    console.log(compSelect)

    if(playerChoice === compSelect){
        alert("It's a tie!")
    }else if(playerChoice === 'rock'){
        if(compSelect === 'scissors'){
            alert("You win!")
        }else if(compSelect === 'paper'){
            alert("You lose.")
        }
    }else if(playerChoice === 'paper'){
        if(compSelect === 'rock'){
            alert("You win!")
        }else if(compSelect === 'scissors'){
            alert("You lose.")
        }
    }else if(playerChoice === 'scissors'){
        if(compSelect === 'paper'){
            alert("You win!")
        }else if(compSelect === 'rock'){
            alert("You lose.")
        }
    }
    choiceInput.value = ''
})