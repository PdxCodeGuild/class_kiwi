console.log("start of code")

const shuffleBtn = document.querySelector("#shuffle-btn")
const dealBtn = document.querySelector("#deal-btn")
let deckID = null
let hands = {
    dealer: [],
    player: []
}

// getCards is a function. leave the () off so it is activated by the click
shuffleBtn.addEventListener("click", getCards)

dealBtn.addEventListener("click", dealCards)

// this returns a promise causing the app to run out of order and require the .then
// fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
// .then(function(data) {
//     return data.json()
//   }       
// ).then(function(data){
//     console.log(data)
// })

// async forces the app to go line by line instead of spinning off other threads
async function getCards() {
    // await tells the code to hold on until there is a return from the fetch
    const response = await fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    const data = await response.json()
    console.log(data)
    deckID = data.deck_id
}

async function dealCards(){
    // the `${}` acts like an f string in python
    const url = `https://deckofcardsapi.com/api/deck/${deckID}/draw/?count=4`
    const response = await fetch(url)
    const data = await response.json()

    hands.dealer = data.cards.splice(0,2)
    hands.player = data.cards
    showcards()
    showcards(true)
    // console.log(data)
}

function showcards(dealer = false){
    const hand = dealer ? hands.dealer : hands.player
    const selector = dealer ? "#dealer" : "#player"
    const handContainer = document.querySelector(selector) 
    handContainer.innerHTML = ""
    for (card of hand){
        const cardImg = document.createElement('img')
        cardImg.src = card.image
        handContainer.append(cardImg)
    }
}




console.log("end of code")