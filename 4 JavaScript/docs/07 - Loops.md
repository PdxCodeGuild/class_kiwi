
# Loops

- [While-Loops](#while-loops)
- [For-Loops](#for-loops)
  - [Iterating over a String](#iterating-over-a-string)
  - [Iterating over an Array](#iterating-over-an-array)
  - [Iterating over an Object](#iterating-over-an-object)
- [Continue and Break](#continue-and-break)

## While-Loops

While-loops will run while the given condition is `true`.

```javascript
let i = 0
while (i < 5) {
    console.log(i)
    i++
}
```
> 0
> 1
> 2
> 3
> 4


## For-Loops

For-loops have three parts, separated by semi-colons. The first is the **initialization**, the second is the **condition** and the third is the **increment**. These are simply the parts of the `while` loop from above re-arranged.

```javascript
// for (initialization; condition; increment)
for (let i=0; i<5; ++i) {
    console.log(i)
}
```
> 0
> 1
> 2
> 3
> 4

### Iterating over a String

```javascript
//       01234
let s = 'hello'

// iterate over the indices of the characters of a string using a while-loop
let i = 0
while (i < s.length) {
    console.log(s[i])
    i++
}
// iterate over the indices of the characters of a string using a for-loop
for (let i=0; i<s.length; i++) {
    console.log(s[i])
}
// iterate over the indices of a string using for-in
for (i in s) {
    console.log(s[i])
}
// iterate over the characters of a string using for-of
for (char of s) {
    console.log(char)
}
```

### Iterating over an Array

```javascript
let fruits = ['apples', 'bananas', 'plums']
// iterate over the indices of an array using a while-loop
let i=0
while (i < fruits.length) {
    console.log(fruits[i])
    i++
}
// iterate over the indices of an array
for (let i=0; i<fruits.length; i++) {
    console.log(fruits[i])
}
// iterate over the indices using for-in
for (i in fruits) {
    console.log(fruits[i])
}
// iterate over the elements using for-of
for (fruit of fruits) {
    console.log(fruit)
}
```

### Iterating over an Object


```javascript
let fruits = {
    'apples': 1.0,
    'bananas': 1.5,
    'plums': 1.25
}
// iterate over the keys/properties of an object
for (key in fruits) {
    console.log(key + ' ' + fruits[key])
}
// apples 1
// bananas 1.5
// plums 1.25
```


## Continue and Break

The `continue` keyword will skip the rest of the current iteration and start with the next iteration.

```javascript
let nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for (let i=0; i<nums.length; ++i) {
    if (nums[i]%2 == 1) {
        continue
    }
    console.log(nums[i])
}
```
> 0
> 2
> 4
> 6
> 8


The `break` keyword will skip the rest of the current iteration and leave the loop.

```javascript
let nums = [1, 2, 3, 4, 5, 6, 7, 8]
for (let i=0; i<nums.length; ++i) {
    if (nums[i]%2 == 1) {
        break
    }
    console.log(nums[i])
}
```
> 0