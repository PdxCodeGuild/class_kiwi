// get selection buttons
const selectionButtons = document.querySelectorAll('[data-selection]')

const finalColumn = document.querySelector('[data-final-column]')
// create an array of all possible selections
const SELECTIONS = [
    {
        name:'rock',
        emoji: '🗿',
        beats: 'scissors'
    },
    {
        name:'paper',
        emoji: '📜',
        beats: 'rock'
    },
    {
        name:'scissors',
        emoji: '✂️',
        beats: 'paper'
    },
    
]

selectionButtons.forEach(selectionButtons => {
    selectionButtons.addEventListener('click', e => {
        const selectionName = selectionButtons.dataset.selection
        // retrieve individual selection by looping through all selections
        const selection = SELECTIONS.find(selection => selection.name === selectionName)
        makeSelection(selectionName)
    })
})

function makeSelection(selection){
    const computerSelection = randomSelection()
    const yourWinner = isWinner(selection, computerSelection)
    const computerWinner = isWinner(computerSelection, selection )

    addSelectionResult(computerSelection, computerWinner)
    addSelectionResult(selection, yourWinner)

    if(yourWinner) incrementscore(yourscorespan)
    if(computerWinner) incrementscore(computerscorespan)
    // console.log(selection)
}

// function to increment score

function incrementscore (scorespan) {
    scorespan.innerText = parseInt(scorespan.innerText) +1
}

// automate computer selection 

function randomSelection() {
    const randomIndex = Math.floor(Math.random() * SELECTIONS.length) // provide an index from our array 
    return SELECTIONS[randomIndex]
}

// create logic for determining the winner 
function isWinner(selection, opponentSelection){
    return selection.beats === opponentSelection.name
}

// create a function to provide results

function addSelectionResult (selection, winner) { 
    const div = document.createElement('div')
    div.innerText = selection.emoji
    div.classList.add('result-selection')
    if (winner) div.classList.add('winner')
    finalColumn.after(div)
}