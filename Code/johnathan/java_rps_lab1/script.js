// get selection buttons
const selectionButtons = document.querySelectorAll('[data-selection]')
// create an array of all possible selections
const SELECTIONS = [
    {
        name:'rock',
        emjoi: '🗿',
        beats: 'scissors'
    },
    {
        name:'paper',
        emjoi: '📜',
        beats: 'rock'
    },
    {
        name:'scissors',
        emjoi: '✂️',
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

    console.log(selection)
}


// automate computer selection 

function randomSelection() {
    const randomIndex = Math.random() * SELECTIONS.length // provide an index from our array 
    return SELECTIONS[randomIndex]
}

// create logic for determining the winner 
function isWinner(selection, opponentSelection){
    return selection.beats === opponentSelection.name
}

// create a function to provide results

function addSelectionResult (selection, winner)