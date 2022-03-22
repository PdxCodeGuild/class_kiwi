
# Vue Snowman

Let's write a program to play a game of [Snowman](https://en.wikipedia.org/wiki/Snowman_(game))! Snowman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.


We can use [Axios](../docs/13%20-%20APIs%20and%20Ajax.md#ajax-in-axios) to send a request to this random word API.

```
https://random-word-api.herokuapp.com/word/?swear=0
```

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. Allow the user 10 tries to guess the letters of the word. If the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

We could either have an input field and button for making a guess, or have a button for every letter and disable it after guessing.

For images, [this page](https://www.hanginghyena.com/snowman) has a series of images that can be linked to.