//defining cc number for testing 
//   4556737586899855
let cc1 = prompt("Please enter Credit Card Number")
alert(`Credit Card Number: ${cc1}`)

//convert to array of ints
cc1 = cc1.split('')
let cc=[]
for (let x =0; x<cc1.length;x++){
  cc.push(parseInt(cc1[x]))
}
alert(`Card Number as Array of Intergers: ${cc}`)

//slice off last digit as check digit. 
check_digit = cc.pop()
alert(`Check Digit: ${check_digit}`)
//reverse the array
cc = cc.reverse()
alert(`Number Reversed: ${cc}`)

//double every other element in the reverse list
let output=[]
cc.forEach(function(digit,i){
  if (i % 2 == 0){
    output.push(digit*2)
  }
  else{
    output.push(digit)
  }

})

alert(`Doubling: ${output}`)

//subtract nine from numbers over nine
let over_nine=[]
for (let x =0;x<output.length; x++){
  if (output[x] > 9){
    over_nine.push(output[x]-9)
  }else{
    over_nine.push(output[x])
  }
}
alert(`Subtracting Nine: ${over_nine}`)

//Sum all values
let sum =0;
for (let x =0; x < over_nine.length; x++){
  sum += over_nine[x];
}
alert(`Sum of All Values: ${sum}`)

//take second digit of sum 
sum =sum.toString()
let secondDigit = sum[1]
console.log(`second digit from sum: ${secondDigit}`)
sum =parseInt(sum)

let check = function(a,b){
  if (a == b){
    return 'True Valid'
  }else{
    return 'False InValid'
  }

}
answer = check(secondDigit,check_digit)
alert(`${answer}`)


