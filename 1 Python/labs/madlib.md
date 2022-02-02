# Lab 2: Mad Libs

Write a simple program that prompts the user for several inputs then
 prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.

## Instructions

1. Search the interwebs for an example Mad Lib
2. Ask the user for each word you'll put in your Mad Lib
3. Use `string concatenation` to put each word into the Mad Lib

## Example:

```
>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.
```


## Version 2 (optional)

* Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
* Add randomness! Use the random module, rather than selecting which adjective goes where in the story.


## Version 3 (optional)
* Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.


## Key Concepts

- Variables
- String formatting
- Handling user input