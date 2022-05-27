
const shuffleBtn = document.querySelector("#shuffle-btn")
const dealBtn = document.querySelector("#deal-btn")
let deckID = null
let hands = {
    dealer: [],
    player: []
}

shuffleBtn.addEventListener("click", getCards)

dealBtn.addEventListener("click", dealCards)

async function dealCards() {
    const url = `https://deckofcardsapi.com/api/deck/${deckID}/draw/?count=2`
    const response = await fetch(url)
    const data = await response.json()

    hands.dealer = data.cards
    showCards()
}

function showCards(dealer = false) {
    const hand = hands.dealer
    const handContainer = document.querySelector("#dealer")
    handContainer.innerHTML = ""

    for (card of hand){
        const cardImg = document.createElement('img')
        cardImg.src = card.image
        handContainer.append(cardImg)
    }
}

async function getCards() {
    const response = await fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    const data = await response.json()
    console.log(data)
    deckID =data.deck_id
}

// console.log("start of code")

// fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
// .then(function (data) {
//     return data.json()
//     }
// ).then(function (data) {
// console.log(data)
// })