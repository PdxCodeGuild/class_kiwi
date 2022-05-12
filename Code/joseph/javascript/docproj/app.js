console.log("start of code")

const shuffleBtn = document.querySelector("#shuffle-btn")
const drawBtn = document.querySelector("#draw-btn")
let deckID = null
let card = []
let cardsLeft = []

shuffleBtn.addEventListener("click", getDeck)
drawBtn.addEventListener("click", drawCard)

async function drawCard() {
    const url =`https://deckofcardsapi.com/api/deck/${deckID}/draw/?count=52`
    const response = await fetch(url)
    const data = await response.json()
    card = data.cards
    cardsLeft = data.cards.slice(1, 52)
    showCard()
    console.log(data)
}

function showCard() {
    const cardContainer = document.querySelector("#original-card")
    cardContainer.innerHTML = ""
    const cardText = document.createElement('h5')
    cardText.textContent = 'Your Original Card'
    cardContainer.append(cardText)
    const cardImg = document.createElement('img')
    cardImg.src = card[0].image
    cardContainer.append(cardImg)
    console.log(card)
    pmCard100()
}

function pmCard100() {
    const cardContainer = document.querySelector("#pm-card-100")
    cardContainer.innerHTML = ""
    const cardText = document.createElement('h5')
    cardText.textContent = '10x10 Photomosaic'
    cardContainer.append(cardText)
    const cardImg = document.createElement('img')
    cardImg.src = cardsLeft[0].image
    cardContainer.append(cardImg)
    // console.log(card)
    pmCard10000()
}

function pmCard10000() {
    const cardContainer = document.querySelector("#pm-card-10000")
    cardContainer.innerHTML = ""
    const cardText = document.createElement('h5')
    cardText.textContent = '100x100 Photomosaic'
    cardContainer.append(cardText)
    const cardImg = document.createElement('img')
    cardImg.src = cardsLeft[1].image
    cardContainer.append(cardImg)
    // console.log(card)
    pmCard70964()
}

function pmCard70964() {
    const cardContainer = document.querySelector("#pm-card-70964")
    cardContainer.innerHTML = ""
    const cardText = document.createElement('h5')
    cardText.textContent = '314x226 Photomosaic'
    cardContainer.append(cardText)
    const cardImg = document.createElement('img')
    cardImg.src = cardsLeft[2].image
    cardContainer.append(cardImg)
    // console.log(card)
}

async function getDeck() {
    const response = await fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    const data = await response.json()
    console.log(data)
    deckID = data.deck_id
}


console.log("end of code")