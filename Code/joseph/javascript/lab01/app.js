let password=document.getElementById("rpg");

function genPassword() {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()";
    let passwordLength = Number(prompt("Please set a password length", "12"));
    let password = "";
    for (let i = 0; i <= passwordLength; i++) {
    let randomNumber = Math.floor(Math.random() * chars.length);
    password += chars.substring(randomNumber, randomNumber +1);
}
    document.getElementById("rpg").value = password;
}
