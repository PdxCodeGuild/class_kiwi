

# Guess the Number (Vue)

Let's build a 'guess the number' game in Vue!


## Part 1

Use Vue's `v-for` to generate the buttons for our game. This can be used with an array, but it can also be used with a number. For example, the code below will produce 5 div's.

```html
<div v-for="i in 5">{{i}}</div>
```

When the page loads, generate a [random number](../docs/03%20-%20Numbers%20and%20Arithmetic.md#random-numbers) between 1 and 10. Every time the user presses one of these buttons, check if the chosen number was correct and if so tell the user they've won.

It's possible to pass parameters to app methods, so we can pass the button's number to a method to check if it's correct.
```html
<button v-on:click="myMethod('hello world')">
<script>
    let app = new Vue({
        methods: {
            myMethod: function(text) {
                alert(text)
            }
        }
    })
</script>
```

## Part 2

When the user guesses the correct answer, tell them how many guesses it took and generate a new random number to reset the game.


## Part 3

Allow the user to enter in the number range before starting the game. For example, the user could enter in `20` and the game would generate 20 buttons.

## Part 4


Each time the user presses a button, disable it. This can be accomplished several ways, but one way is to use an array of booleans to generate the buttons. We can then iterate over the array elements and indices when generating our buttons. When the user clicks a button, flip the boolean.

```html
<div v-for="(bt, index) in buttons">{{ index }}</div>
```

Another option would be to represent the data for each button as an array of objects (generated in the app's `created` lifecycle hook), each containing an index and a boolean indicating whether it's disabled (e.g. `{index: 3, disabled: false}`).

When the game is over, re-enable all the buttons.


