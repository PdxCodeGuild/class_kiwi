

# Numbers and Arithmetic



1. [Numbers](#numbers)
2. [Arithmetic Operators](#arithmetic-operators)
3. [Pre-Increment vs Post-Increment](#pre-increment-vs-post-increment)
4. [Math](#math)
5. [Random Numbers](#random-numbers)

## Numbers

Other languages distinguish between `int` and `float`, JavaScript only has `number`. [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)

```javascript
let x = 1
let y = 1.5
let z = 1.23e-3
```

## Arithmetic Operators


Unlike other languages, JavaScript doesn't have a special 'int' type, only a 64-bit float type called `number`. There are 5 arithmetic operators, addition, subtraction, multiplication, division, and modulus. The modulus of `a` and `b` (`a%b`) is the remainder of `a/b`. You can read more about arithmetic [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators)

```javascript
5 + 1 // 6
5 - 1 // 4
2 * 3 // 6
3 / 2 // 1.5
2 % 3 // 2
```

There are also operations which edit the value of the original variable.

```javascript
let a = 1
a += 3  // a = a + 3
a -= 2  // a = a - 2
a *= 5  // a = a * 5
a /= 10 // a = a / 10
a++     // a = a + 1, a += 1
++a     // a = a + 1, a += 1
a--     // a = a - 1, a -= 1
--a     // a = a - 1, a -= 1
```


## Pre-Increment vs Post-Increment

There is a different between `x++` (post-increment) and `++x` (pre-increment) in how they work with compound statements. With pre-increment, the increment occurs, and then the rest of the expression is evaluated. With post-increment, the expression is evaluated, and then the increment occurs. If you want to avoid worrying about it, just don't write compound statements with the `++` operator.

```javascript
let x = 5
console.log('my number is ' + x++) // my number is 5
x = 5
console.log('my number is ' + ++x) // my number is 6
```


## Math

The built-in object `Math` has additional operations that can be performed on numbers. You can read more about `Math` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math).

```JavaScript
Math.abs(-4)    // 4 - absolute value
Math.sqrt(16)   // 4.0 - square root
Math.min(5, 6)  // 5 - the smaller of the two
Math.max(5, 6)  // 6 - the larger of the two
Math.floor(4.5) // 4 - always round down
Math.ceil(4.5)  // 5 - always rounds up
Math.round(4.5) // 5 - round to the nearest integer
Math.random()   // get a random number between 0 and 1, but not including 1
Math.pow(5, 2)  // 25 - exponentiation
Math.PI         // 3.1415... pi
Math.sin(0)     // 0.0 - sine operator
Math.cos(0)     // 1.0 - cosine operator
```

## Random Numbers

```javascript
console.log(Math.random()) // random number between 0 and 1
console.log(Math.random()*20) // random number between 0 and 20
console.log(20 + Math.random()*20) // random number between 20 and 40
console.log(Math.floor(20 + Math.random()*20)) // random *integer* between 20 and 40
let letters = ['a', 'b', 'c']
console.log(letters[Math.floor(Math.random()*letters.length)]) // random element

function randint(a, b) {
    return Math.floor(a + Math.random()*(b-a+1))
}

function randomChoice(arr) {
    let i = randint(0, arr.length-1)
    return arr[i]
}

let x = randint(1, 10) // a random number between 1 and 10
console.log(x)

let fruits = ['apples', 'bananas', 'pears']
console.log(randomChoice(fruits)) // get a random element out of an array
```
