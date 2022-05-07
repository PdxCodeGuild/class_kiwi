// JavaScript redo lab of ROT13 cypher

// Accept input
let user_string = prompt("Please enter a message: ")

// Make it all lower case
user_string = user_string.toLowerCase()

// Dictionary
/*
let letter_values = {
    y : 'a',
    o : 'd',
    d : 'o',
    a : 'y'
}
*/
let letter_values = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'n' : 'a',
    'o' : 'b',
    'p' : 'c',
    'q' : 'd',
    'r' : 'e',
    's' : 'f',
    't' : 'g',
    'u' : 'h',
    'v' : 'i',
    'w' : 'j',
    'x' : 'k',
    'y' : 'l',
    'z' : 'm'
}
// console.log(letter_values)
// set null variable
let coded_word = ""
// Meat Grinder
function rot13(input) {
    for (letter of input){
        // console.log(letter, letter_values[letter])
        coded_word += letter_values[letter] 
    }
    return coded_word
}

let finished = rot13(user_string)
alert(finished)
// console.log(coded_word)
// console.log("string")