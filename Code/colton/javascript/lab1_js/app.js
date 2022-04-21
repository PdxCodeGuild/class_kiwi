//variables 

const choices = ['Rock', 'Paper', 'Scissors']
const button = document.querySelector('#rock')
const button2 = document.querySelector('#paper')
const button3 = document.querySelector('#scissors')
const computerChoice = document.querySelector('.computer-choice')
const result = document.querySelector('.result')


//functions

function randomChoice(){
    let computerAns = choices[Math.floor(Math.random()*3)]
    return computerAns
}

function getResult(userChoice, compAns){
    if(userChoice===compAns){
        return 'Tie'
    }
    else if(userChoice==='Scissors'&& compAns==='Paper'){
        return 'You Win'
    }
    else if(userChoice==='Scissors'&& compAns==='Rock'){
        return 'You Lose'
    }
    else if(userChoice==='Rock'&& compAns==='Scissors'){
        return 'You Win'
    }
    else if(userChoice==='Rock'&& compAns==='Paper'){
        return 'You Lose'
    }
    else if(userChoice==='Paper'&& compAns==='Rock'){
        return 'You Win'
    }
    else if(userChoice==='Paper'&& compAns==='Scissors'){
        return 'You Lose'
    }


    return 
}



//listeners

button.addEventListener('click', function(){
    let userChoice = 'Rock'
    let compAns = randomChoice()
    computerChoice.innerText = `${compAns}`
    result.innerText = `${getResult(userChoice, compAns)}`
})


button2.addEventListener('click', function(){
    let userChoice = 'Paper'
    let compAns = randomChoice()
    computerChoice.innerText = `${compAns}`
    result.innerText = `${getResult(userChoice, compAns)}`
})

button3.addEventListener('click', function(){
    let userChoice = 'Scissors'
    let compAns = randomChoice()
    computerChoice.innerText = `${compAns}`
    result.innerText = `${getResult(userChoice, compAns)}`
})