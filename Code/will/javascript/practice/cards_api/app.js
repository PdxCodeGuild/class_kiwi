const shuffleBtn = document.querySelector("#shuffle-btn")
const dealBtn = document.querySelector("#deal-btn")
let deckID = null
let hands = {
    dealer: [],
    player: []
}


shuffleBtn.addEventListener("click", getCards)
dealBtn.addEventListener("click", dealCards)


///// ASYNC WAIT METHOD /////
async function getCards(){
    const response = await fetch("http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6")
    const data = await response.json()
    console.log(data)
    deckID = data.deck_id
}


async function dealCards(){
    const url = `http://deckofcardsapi.com/api/deck/${deckID}/draw/?count=4`
    const response = await fetch(url)
    const data = await response.json()

    hands.dealer = data.cards.splice(0, 2)
    hands.player = data.cards
    console.log(data)
    playerValue = showCards()
    dealerValue = showCards(true)
    whoWins(playerValue, dealerValue)
}


function addHand(value){
    const strValue = value
    let intValue = 0
    if(strValue == 'KING'){
        intValue =10
    }else if(strValue == 'QUEEN'){
        intValue =10
    }else if(strValue == 'JACK'){
        intValue = 10
    }else if(strValue == 'ACE'){
        intValue = 11
    }else{
        intValue = parseInt(value)
    }
    return intValue
}





function showCards(dealer = false){
    const hand = dealer ? hands.dealer : hands.player
    const selector = dealer ? '#dealer' : '#player'
    let handValue = 0
    const handContainer = document.querySelector(selector)
    handContainer.innerHTML = ''

    for(card of hand){
        const cardImage = document.createElement('img')
        cardImage.src = card.image
        handContainer.append(cardImage)
        cardValue = addHand(card.value)
        handValue += cardValue
    }
    return handValue
}


function whoWins(playerValue, dealerValue){
    if(playerValue > dealerValue && playerValue <= 21){
        alert('You Win!')
    }else if(dealerValue > playerValue && dealerValue <= 21){
        alert('Dealer Wins.')
    }else if(dealerValue = playerValue){
        alert('Push.')
    }
}





///// DOT THEN METHOD /////
// fetch("http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
// .then(function(data){
//     return data.json()
// }
// ).then(function(data){
//     console.log(data)
// })
