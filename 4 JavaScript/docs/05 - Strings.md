
# Strings


- [Overview](#overview)
- [Escape Sequences](#escape-sequences)
- [Template Literals](#template-literals)
- [Line Continuation](#line-continuation)
- [String Methods](#string-methods)
  - [Accessing Characters: `s[index]`, `s.charAt(index)`](#accessing-characters-sindex-scharatindex)
  - [Concatenation: `s1+s2`, `s1.concat(s2, s3, ...)`](#concatenation-s1s2-s1concats2-s3-)
  - [Repeat: `s.repeat(count)`](#repeat-srepeatcount)
  - [Index of a Substring: `s1.indexOf(s2)`, `s1.lastIndexOf(s2)`](#index-of-a-substring-s1indexofs2-s1lastindexofs2)
  - [Includes: `s1.includes(s2)`](#includes-s1includess2)
  - [Starts-With and Ends-With: `s1.startsWith(s2)`, `s1.endsWith(s2)`](#starts-with-and-ends-with-s1startswiths2-s1endswiths2)
  - [Changing Case: `s.toUpperCase()`, `s.toLowerCase()`](#changing-case-stouppercase-stolowercase)
  - [Replace: `s1.replace(s2, s3)`, `s1.replaceAll(s2, s3)`](#replace-s1replaces2-s3-s1replacealls2-s3)
  - [Split: `s.split(delimiter)`](#split-ssplitdelimiter)
  - [Ascii Codes: `s.charCodeAt(index)`, `String.fromCharCode(code)`](#ascii-codes-scharcodeatindex-stringfromcharcodecode)
  - [Substring: `s.substring(start, end)`, `s.slice(start, end)`, `substr(start, length)`](#substring-ssubstringstart-end-sslicestart-end-substrstart-length)
  - [Trim: `s.trim()`](#trim-strim)


## Overview

Strings represent text, and can be enclosed in either double-quotes or single-quotes. You can read more about strings [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) and [here](https://www.w3schools.com/js/js_strings.asp).

```javascript
let a = 'hello world!'
let b = "hello world!"
```
## Escape Sequences

Escape sequences allow us to enter special characters into our strings.


| Escape Sequence | Description |
| --- | --- |
| `\n` | newline |
| `\t` | tab |
| `\'` | single-quote |
| `\"` | double-quote |
| `\\` | backslash |
| `\0` | begins an octal character |
| `\x` | begins a hexidecimal character |
| `\u` | begins a unicode character (e.g. `\u2665` is `♥`) |



## Template Literals

Template Literals allow us to more easily inject variables into strings. Template Literals are defined via back-ticks `. More info [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).


```javascript
function getFullName(title, fname, lname, degree) {
    return `${title} ${fname} ${lname}, ${degree}`
}
// returns 'Rear Admiral Grace Hopper, PhD'
getFullName('Rear Admiral', 'Grace', 'Hopper', 'PhD')
```

You can even write expressions inside the template:
```javascript
function showYourWork(num1, num2) {
    return `${num1} + ${num2} = ${num1 + num2}`
}
// returns '3 + 4 = 7'
showYourWork(3, 4)
```

## Line Continuation

A backslash followed by a newline in a string literal will continue that string. The resulting string won't contain a backslash or a newline.

```javascript
let s = 'this is a really long\
string, so long that we had to\
write it on multiple lines'
```

You may also use a template literal to get a multi-line string, which **will** contain new-line characters.

```javascript
let s = `this is a really long
string, so long that we had to
write it on multiple lines`
```

## String Methods

Below are some common operations that can be performed on strings, you can also find a list [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods) and [here](https://www.w3schools.com/js/js_string_methods.asp).


### Accessing Characters: `s[index]`, `s.charAt(index)`

We can get a character at a given index using square brackets `[]` or `charAt`. [more info](https://stackoverflow.com/questions/5943726/string-charatx-or-stringx)

```javascript
//          01234
let text = 'hello'
console.log(text[0]) // h
console.log(text[1]) // e
console.log(text.charAt(0)) // h
```

### Concatenation: `s1+s2`, `s1.concat(s2, s3, ...)`

We can combine strings together using the `+` operator or the `concat` method.

```javascript
let s = 'hello' + ' ' + 'world'
console.log(s) // hello world

s = 'hello'.concat(' ', 'world')
console.log(s) // hello world
```

This can also be used with numbers, booleans, etc.

```javascript
let s = 'My age is ' + 30
console.log(s) // My age is 30
```

### Repeat: `s.repeat(count)`

The `repeat` method allows us to repeat a string.

```javascript
let s = 'hello'
console.log(s.repeat(5)) // hellohellohellohellohello
```

### Index of a Substring: `s1.indexOf(s2)`, `s1.lastIndexOf(s2)`

The `indexOf` and `lastIndexOf` methods return the index of the first and last occurrence respectively.

```javascript
//       0123456789...
let s = 'hello world, hello moon'
console.log(s.indexOf('hello')) // 0
console.log(s.indexOf('llo')) // 2
console.log(s.lastIndexOf('hello')) // 13
```

### Includes: `s1.includes(s2)`

The `includes` method returns `true` if the string contains the given substring, `false` if it doesn't.

```javascript
let s = 'hello world'
console.log(s.includes('hello')) // true
console.log(s.includes('goodbye')) // false
```


### Starts-With and Ends-With: `s1.startsWith(s2)`, `s1.endsWith(s2)`

The `startsWith` method returns `true` if the string starts with the given substring, `false` if it doesn't. The `endsWith` method returns `true` if the string ends with the given substring, `false` otherwise.


```javascript
let s = 'hello world'
console.log(s.startsWith('hello')) // true
console.log(s.startsWith('goodbye')) // false
console.log(s.endsWith('world')) // true
```

### Changing Case: `s.toUpperCase()`, `s.toLowerCase()`

The `toLowerCase` method converts a string to lower case. The `toUpperCase` converts a string to upper case.

```javascript
let s = 'Hello World!'
console.log(s.toUpperCase()) // HELLO WORLD!
console.log(s.toLowerCase()) // hello world!
```


### Replace: `s1.replace(s2, s3)`, `s1.replaceAll(s2, s3)`

We can replace the first occurrence of one string with another using `replace`.

```javascript
let text = 'hello world, hello moon'
text = text.replace('hello', 'goodbye')
console.log(text) // goodbye world, hello moon
```

If you want to replace multiple occurrences, you can use `replaceAll`

```javascript
let text = 'hello world, hello moon'
text = text.replaceAll('hello', 'goodbye')
console.log(text) // goodbye world, goodbye moon
```

### Split: `s.split(delimiter)`

The `split` method splits a string into an array of strings, according to the delimiter.

```javascript
let fruits = 'apples bananas plums'
fruits = fruits.split(' ') // split on space
console.log(fruits) // ['apples', 'bananas', 'plums']
```

The opposite operation is `join`, which is an array method.

```javascript
let fruits = ['apples', 'bananas', 'plums']
fruits = fruits.join(', ') // join with a comma-space
console.log(fruits) // apples, bananas, plums
```

### Ascii Codes: `s.charCodeAt(index)`, `String.fromCharCode(code)`

The `charCodeAt` method and `fromCharCode` methods convert between characters and their [ASCII codes](http://www.asciitable.com/).

```javascript
//          01234
let text = 'hello'
console.log(text.charCodeAt(0)) // 104
console.log(text.charCodeAt(1)) // 101
console.log(String.fromCharCode(104)) // h
console.log(String.fromCharCode(101)) // e
```



### Substring: `s.substring(start, end)`, `s.slice(start, end)`, `substr(start, length)`

These three methods return a sub-string, but the `substring` and `slice` take the starting and ending index as parameters, while the `substr` takes the starting index and the length. [more info](https://stackoverflow.com/questions/2243824/what-is-the-difference-between-string-slice-and-string-substring)

```javascript
//       0123456789
let s = 'hello world'
console.log(s.substring(1, 5)) // ello
console.log(s.slice(1, 5)) // ello
console.log(s.substr(1, 4)) // ello
```

### Trim: `s.trim()`

The `trim` method removes whitespace from the beginning and end of a string, but not the middle.

```javascript
let s = '  hello world\n\t '
console.log(s.trim()) // hello world
```



