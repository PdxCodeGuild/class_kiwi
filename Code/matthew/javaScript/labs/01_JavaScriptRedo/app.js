
const options= ['rock','paper','scissors']
let human = ''
const random= Math.floor(Math.random() * options.length)

// results h2
const results= document.querySelector('.results')
// comp h2
const comp= document.querySelector('.comp')

const rock= document.querySelector('.rock')
rock.addEventListener('click',function(){
    let computer= options[Math.floor(Math.random() * options.length)]
    // let human= 'rock'
    if(computer == 'rock'){
        results.innerText= 'Tie'
        comp.innerText= `Computer chose ${computer}`

    }else if(computer == 'paper'){
        results.innerText= 'Computer wins'
        comp.innerText= `Computer chose ${computer}`
    }else{
        results.innerText= 'You win'
        comp.innerText= `Computer chose ${computer}`
    }

})

const paper= document.querySelector('.paper')
paper.addEventListener('click',function(){
    let computer= options[Math.floor(Math.random() * options.length)]
    // let human= "paper"
    if(computer == 'rock'){
        results.innerText= 'you win'
        comp.innerText= `Computer chose ${computer}`
    }else if(computer == 'paper'){
        results.innerText= 'tie'
        comp.innerText= `Computer chose ${computer}`
    }else{
        results.innerText= 'You loose'
        comp.innerText= `Computer chose ${computer}`
    }

})
const scissors= document.querySelector('.scissors')
scissors.addEventListener('click',function(){
    let computer= options[Math.floor(Math.random() * options.length)]
    // let human= "scissors"
    if(computer == 'rock'){
        results.innerText= 'you loose'
        comp.innerText= `Computer chose ${computer}`
    }else if(computer == 'paper'){
        results.innerText= 'you win'
        comp.innerText= `Computer chose ${computer}`
    }else{
        results.innerText= 'Tie'
        comp.innerText= `Computer chose ${computer}`
    }

})

    

