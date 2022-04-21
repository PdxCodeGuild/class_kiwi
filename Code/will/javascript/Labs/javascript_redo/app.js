const button = document.querySelector('#submit')


button.addEventListener('click', function(){
    var compChoices = ['Rock', 'Paper', 'Scissors']
    var compSelect = compChoices[Math.floor(Math.random() * compChoices.length)]
    document.body.innerHTML = compSelect
})
//     let userInput = prompt('Rock, Paper, or Scissors?')

//     if (userInput === 'Rock'){
//         alert
//     }
// })