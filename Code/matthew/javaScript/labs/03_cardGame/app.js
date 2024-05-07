
// selectors
const shuffleBtn= document.querySelector("#shuffle-btn")
const dealBtn= document.querySelector("#deal-btn")
const fishBtn= document.getElementById('fish')
const UserOptions= document.getElementById('user-options')
// const options= document.getElementById('options')
let cardImg = null
let deckId = null
let userContainer = null
let hands= {
    dealer:[],
    player:[]
}
let pairsWon = {
    dealer:[],
    player:[]
}

// listeners
fishBtn.addEventListener('click',fish)
shuffleBtn.addEventListener('click',getCards)
dealBtn.addEventListener('click', dealCards)

// ----------------------------------------------------------------------------

async function dealCards(){
    const url = `https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=14`
    const response = await fetch(url)
    const data= await response.json()
    hands.dealer= data.cards.splice(0, 7)
    hands.player= data.cards
    // console.log(hands.dealer)\
    
    showCards()
    showCards(true)
} 

async function getCards(){
    const response= await fetch('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    const data= await response.json()
    deckId = data.deck_id
    console.log('deck shuffled')
}
// ----------------------------------------------------------------------------

function showCards(dealer = false){
    // 
    const hand = dealer ? hands.dealer : hands.player
    const selector = dealer ? "#dealer" : "#player"
    const handContainer = document.querySelector(selector)
    handContainer.innerHTML= ""
    // getting images for each card
    for (card of hand){
        // creating new img tag
        cardImg = document.createElement('img')
        cardImg.src= card.image
        handContainer.append(cardImg)
    }

}
// ----------------------------------------------------------------------------

function fish(){
    if(userContainer){
        userContainer.remove()
    }
    // creating a dropdown menu
    userContainer = document.createElement('select')
    // give new element id="options"
    userContainer.setAttribute('id','options')
    let hand = []
    playerCards= hands.player
    for (const key in playerCards) {
        // add player cards to hand
    hand.push(playerCards[key].value)
    }

    // for each card in hand array
    for(card of hand){
        // for each card create an option element for dropdown select
        userChoices= document.createElement("option")
        // assign option value="`${card}`"
        userChoices.setAttribute('value', `${card}`)
        userChoices.innerHTML= card
        //adding options to dropdown menu
        userContainer.append(userChoices)
        // adding dropdown menu to fishing div
        UserOptions.append(userContainer)

    }
}
// ----------------------------------------------------------------------------

function goFish(){
    // selecting dropdown element
    selectElement= document.querySelector('#options')
    // getting dropdown element value
    output= selectElement.options[selectElement.selectedIndex].value;


    for(card of hands.dealer){
        if(card.value === output){
            console.log("They match 'dealer'")
            const indexDealer= hands.dealer.indexOf(card)
            pairsWon.player.push(hands.dealer.splice(indexDealer,1))
            console.log(pairsWon.player)
        }
        if(card.image == cardImg.src){
            console.log(cardImg.src)
        }
    }
    for(const playerCard of hands.player){
        for(const test of hands.dealer){
            if(playerCard = test){
                console.log('hello')
            }
        }
        
}
}
