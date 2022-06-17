const userInput = document.querySelector('#user-input')
const button = document.querySelector('#submit')
const resultsList = document.querySelector('#results-list')
// let encryptWord = String(word).toLowerCase().replace(' ', '')


button.addEventListener('click', function(event){
    event.preventDefault()
    const li = document.createElement('li')
    const span = document.createElement('span')
    const word = userInput.value

    // console.log(encrypt(word))
    resultsList.append(encrypt(word))
    
    
})

// span.textContent = resultsList
// li.append(span)
// console.log(cipher)
// console.log(encryptWord)

let text = String(userInput.value).toLowerCase().replace(' ', '')
let cipher = []

function encrypt(text){
    let newEncrypt = []
    
    for(let i=0; i<text.length; i++){
        cipher.push(text[i])
    }
    
    cipher.forEach(function(letter, index){
        console.log(letter)
        // console.log(letter.charCodeAt(index))
        
        
        let encrypt = letter.charCodeAt(letter[index]) +13
        
        
        if(encrypt < 123){ 
            encrypt = String.fromCharCode(encrypt)
            newEncrypt.push(encrypt)
            // console.log(newEncrypt)
        } else if(encrypt >= 122){
            repeat = (encrypt % 122) + 96
            repeat = String.fromCharCode(repeat)
            newEncrypt.push(repeat)
            // console.log(newEncrypt)
        }
    })
    return newEncrypt
}
























