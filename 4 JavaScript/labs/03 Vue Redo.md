

# Vue Redo

Let's redo one of the following Python labs in [Vue](../docs/Vue.md)!

- [Rock, Paper, Scissors](../../1%20Python/labs/05%20Rock%20Paper%20Scissors.md)
  - Have the user choose rock, paper, or scissors, and show the user who won.
- [Rot Cipher](../../1%20Python/labs/11%20Rot%20Cipher.md)
  - Simple version: the user could just input the word to encode.
  - Complex version: the user could also input the amount to rotate by.
- [Unit Converter](../../1%20Python/labs/12%20Unit%20Converter.md)
  - Simple version: the user enters the distance and units and the app shows them the converted distance in meters
  - Complex version: the user also enters output units
- [Random Password Generator](../../1%20Python/labs/06%20Random%20Password%20Generator.md)
  - Simple version: the user just enters in the number of characters in the password
  - Complex version: the user enters the number of uppercase letters, lowercase letters, numbers, and special characters
- [Number to Phrase](../../1%20Python/mob/05%20Number%20to%20Phrase.md)
  - Have the user enter the number (5) and get back the corresponding word in english (five)


**Vue starter template**
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title></title>
    </head>
    <body>
        <div id="app">
            {{ message }}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <script>
            var app = new Vue({
                el: '#app',
                data: {
                    message: 'Hello Vue!'
                },
                methods: {

                },
                created: function() {

                }
            })
        </script>
    </body>
</html>
```
