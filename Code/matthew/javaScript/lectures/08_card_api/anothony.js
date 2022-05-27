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
  const url = `https://deckofcardsapi.com/api/deck/${deckID}/draw/?count=4`
  const response = await fetch(url)
  const data = await response.json()
  hands.dealer = data.cards.splice(0, 2)
  hands.player = data.cards
  showCards()
  showCards(true)

}
// async await method
async function getCards() {
  const response = await fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
  const data = await response.json()
  deckID = data.deck_id
}
function showCards(dealer = false) {
  const hand = dealer ? hands.dealer : hands.player
  const selector = dealer ? "#dealer" : "#player"
  const handContainer = document.querySelector(selector)
  handContainer.innerHTML = ""
  for (card of hand){
    const cardImg = document.createElement('img')
    cardImg.src = card.image
    handContainer.append(cardImg)
  }
  // for (card in hand){
  //   const cardImg = document.createElement('img')
  //   cardImg.src = hand[card].image
  //   handContainer.append(cardImg)
  // }
}
// dot then method
// fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
// .then(function (data) {
//      return data.json()
//  }
// ).then(function (data){
//   console.log(data)
// })