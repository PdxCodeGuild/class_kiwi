
# Arrays



Arrays are ordered collections of elements. They can hold elements of any type, and elements of different types simultaneously. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) and [here](https://www.w3schools.com/jsref/jsref_obj_array.asp).




- [Defining Arrays](#defining-arrays)
- [Array Operations](#array-operations)
  - [Access: `array[index]`](#access-arrayindex)
  - [Assignment: `array[index] = value`](#assignment-arrayindex--value)
  - [Length: `array.length`](#length-arraylength)
  - [Includes: `array.includes(element)`](#includes-arrayincludeselement)
  - [Index Of: `array.indexOf(element)`](#index-of-arrayindexofelement)
  - [Adding Elements: `array.push(element)`, `array.unshift(element)`](#adding-elements-arraypushelement-arrayunshiftelement)
  - [Removing Elements: `array.pop()`, `array.shift()`](#removing-elements-arraypop-arrayshift)
  - [Adding and Removing Elements: `array.splice(index, to_remove, to_add)`](#adding-and-removing-elements-arrayspliceindex-to_remove-to_add)
  - [Joining: `array.join(delimiter)`](#joining-arrayjoindelimiter)
  - [Concatenating Arrays: `array1.concat(array2)`](#concatenating-arrays-array1concatarray2)
  - [Slicing: `array.slice(start, end)`](#slicing-arrayslicestart-end)
  - [Reversing: `array.reverse()`](#reversing-arrayreverse)
  - [Sorting: `array.sort()`](#sorting-arraysort)

## Defining Arrays

Array literals are designated by square-brackets and commas. The indices of an array begin at 0 and go up to the length minus one.

```javascript
// index:   0  1  2
let nums = [2, 1, 3]
// index:       0         1         2
let fruits = ['apple', 'banana', 'plums']
```

## Array Operations

### Access: `array[index]`

You can access an element by using its index:

```javascript
// indices:      0          1       2
let fruits = ['apple', 'banana', 'plums']
console.log(fruits[0]) // apple
console.log(fruits[1]) // banana
console.log(fruits[3]) // undefined
```

### Assignment: `array[index] = value`

```javascript
// indices:      0          1         2
let fruits = ['apples', 'bananas', 'plums']
fruits[0] = 'cherries'
console.log(fruits) // ['cherries', 'bananas', 'pears']
```

### Length: `array.length`

We can get how many elements an array has using the `length` property.

```javascript
// indices:      0          1         2
let fruits = ['apples', 'bananas', 'plums']
console.log(fruits.length) // 3
```

### Includes: `array.includes(element)`

The `includes` method will return `true` if the array contains the given element, `false` otherwise.

```javascript
let fruits = ['apples', 'bananas', 'plums']
console.log(fruits.includes('apples')) // true
console.log(fruits.includes('pears')) // false
```

### Index Of: `array.indexOf(element)`

The `indexOf` method returns the index of the given element, and `-1` if the array doesn't contain it.

```javascript
// indices:      0          1         2
let fruits = ['apples', 'bananas', 'plums']
console.log(fruits.indexOf('apples')) // 0
console.log(fruits.indexOf('bananas')) // 1
console.log(fruits.indexOf('pears')) // -1
```

### Adding Elements: `array.push(element)`, `array.unshift(element)`

The `push` method places a new element into the array at the end, while the `unshift` method places a new element at the beginning.

```javascript
let fruits = ['apples', 'bananas', 'plums']
fruits.push('pears')
console.log(fruits) // ['apples', 'bananas', 'plums', 'pears']
fruits.unshift('cherries')
console.log(fruits) // ['cherries', 'apples', 'bananas', 'plums', 'pears']
```

### Removing Elements: `array.pop()`, `array.shift()`

The `pop` method removes an element from the end of an array and returns it, while the `shift` method removes an element from the beginning and returns it.

```javascript
let fruits = ['apples', 'bananas', 'plums']
console.log(fruits.pop()) // plums
console.log(fruits) // ['apples', 'bananas']
console.log(fruits.shift()) // apples
console.log(fruits) // ['bananas']
```


### Adding and Removing Elements: `array.splice(index, to_remove, to_add)`

The `splice` method can be used to both add and remove elements from an array.

```javascript
let fruits = ['apples', 'bananas', 'pears', 'plums']
console.log(fruits.splice(1, 2)) // ['bananas', 'pears']
console.log(fruits) // ['apples', 'plums']
console.log(fruits.splice(1, 0, 'cherries')) // []
console.log(fruits) // ['apples', 'cherries', 'plums']
```

### Joining: `array.join(delimiter)`

The `join` method will combine the elements of an array into a single string, separated by the given delimiter.

```javascript
let fruits = ['apples', 'bananas', 'plums']
console.log(fruits.join('_')) // apples_bananas_plums

```

Neither the elements nor the delimiter need to be strings.

```javascript
let random = [1, 2, false]
console.log(random.join(null)) // 1null2nullfalse
```

- `join(delimeter)` turns the array into a string, with elements separated by `delimeter`

### Concatenating Arrays: `array1.concat(array2)`



The `concat` method will combine multiple arrays into a single array.

```javascript
console.log([1, 2, 3].concat([4, 5, 6])) // [1, 2, 3, 4, 5, 6]
console.log([1, 2].concat([3, 4], [5, 6])) // [1, 2, 3, 4, 5, 6]
```


### Slicing: `array.slice(start, end)`

The `slice(start, end)` method returns an array containing a subset of the original array, starting at `start` and ending at `end`. This does not alter the original array.

```javascript
// indices:      0          1         2        3          4
let fruits = ['apples', 'bananas', 'plums', 'pears', 'cherries']
console.log(fruits.slice(1, 3)) // ['bananas', 'plums']
```

### Reversing: `array.reverse()`

The `reverse()` reverses an array.

```javascript
let fruits = ['apples', 'bananas', 'plums', 'pears', 'cherries']
fruits.reverse() // ['cherries', 'pears', 'plums', 'bananas', 'apples']
```

### Sorting: `array.sort()`

The `sort()` sorts an array in **alphabetical** order.

```javascript
let fruits = ['plums', 'bananas', 'pears', 'apples', 'cherries']
fruits.sort()
console.log(fruits) // ['apples', 'bananas', 'cherries', 'pears', 'plums']
```

This can lead to some surprising results when sorting numbers:

```javascript
let nums = [20, 10, 102]
nums.sort()
console.log(nums) // [10, 102, 20]
```

The proper way to sort an array of numbers is by supplying a callback function which tells `sort` the order. This function takes two parameters `a` and `b`, which are elements of the array, and should return a negative number if `a` goes before `b`, a positive number if `a` goes after `b`, or `0` if they're equal.

```javascript
let nums = [20, 10, 102]
nums.sort(function(a, b) {
  if (a < b) {
    return -1
  } else if (a > b) {
    return 1
  } else {
    return 0
  }
})
console.log(nums) // [10, 20, 102]
```

A shorter way to write this would be to just subtract one number from the other.


```javascript
let nums = [20, 10, 102]
nums.sort((a, b) => a - b)
console.log(nums) // [10, 20, 102]
```

