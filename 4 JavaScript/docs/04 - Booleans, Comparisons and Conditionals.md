
# Booleans, Comparisons, and Conditionals

- [Booleans](#booleans)
- [Comparisons](#comparisons)
- [Boolean Operators](#boolean-operators)
- [Type Coercion](#type-coercion)
- [Conditionals](#conditionals)
- [Truthy and Falsey](#truthy-and-falsey)
- [Ternary Operator](#ternary-operator)

## Booleans

Booleans are true/false values. Boolean literals are `true` and `false`.

## Comparisons

You can compare values using comparison operators.

- `==` equal-to, may coerce types
- `===` equal-to, does not coerce types
- `!=` not-equal, may coerce types
- `!==` not-equal, does not coerce types
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to

## Boolean Operators

There are three boolean operators: 'and' `&&`, 'or' `||` and 'not' `!`.

```javascript
let x = 5
if (x > 0 && x < 10) {
    console.log('x is between 5 and 10')
}

if (x == 5 || x == 6) {
    console.log('x is 5 or 6')
}

let y = false
if (!y) {
    console.log('y is false')
}
```


## Type Coercion

If the two operands of `==` aren't of the same type, the JavaScript interpreter will try to convert them to the same type so they can be compared. This may result in unexpected behavior. In practice, it's better to use `===` which will only be true if both operands are of the **same type and value**. [more info](https://stackoverflow.com/questions/359494/which-equals-operator-vs-should-be-used-in-javascript-comparisons)

```javascript
console.log(5 == '5') // true
console.log(5 == 5) // true
console.log(5 === '5') // false
console.log(5 === 5) // true
```


## Conditionals

Conditionals in JavaScript require parantheses and curly-braces.

```javascript
let temperature = 56
if (x < 60) {
    alert('cold')
} else if (x < 80) {
    alert('warm')
} else {
    alert('hot')
}
```

## Truthy and Falsey

JavaScript lets you pass non-boolean types into conditionals, which may evaluate to true or false, depending on what generally makes sense. All values are 'truthy' except `false`, `0`, `""`, `null`, `undefined`, and `NaN`.

```javascript
let x = 0
if (x) {
    console.log('true!')
} else {
    console.log('false!') // this will be called, 0 is falsey
}
```


## Ternary Operator

There's also a ternary operator, which will let you perform an if-else in one line.

```javascript
function min(a, b) {
    return (a < b)? a: b
}
```
