const letters = 'abcdefghijklmnopqrstuvwxyz'
let cipherResult = ''
let resultText = document.querySelector('#results')
const button = document.querySelector('#submit-btn')

button.addEventListener('click', (e) => {
  e.preventDefault()
  const cipherText = document.querySelector('.cipher-text').value.toLowerCase()
  const rotation = parseInt(document.querySelector('.rotation').value)

  for (i = 0; i < cipherText.length; i++) {
    const index = letters.indexOf(cipherText[i])
    cipherResult += letters[(index + rotation) % 26]
  }
  resultText.textContent = `The ciphered result is:  ${cipherResult}`
})