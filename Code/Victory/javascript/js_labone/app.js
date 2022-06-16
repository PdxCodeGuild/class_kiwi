// No need to create query selector since html will be pulling directly from the function
// In conjunction with class, used source code from below---https://dev.to/code_mystery/random-password-generator-using-javascript-6a


function createPassword(){

    const letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}:;',./<>?"
    let lenPassword = 8
    let genPassword = ""
    for (let x = 0; x <= lenPassword; x++) {
        randomNum = Math.floor(Math.random() * letters.length)
        genPassword += letters.substring(randomNum, randomNum+1)
    }
 
    document.getElementById("passw").value=genPassword
    // password=document.getElementById("passw").value; ---> Need to find out why this fails but above works
}


