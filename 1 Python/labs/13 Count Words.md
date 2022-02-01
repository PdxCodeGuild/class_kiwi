

# Lab 15: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on [Project Gutenberg](http://www.gutenberg.org) and navigate to the plain-text version. You can then send a request to that *url* using the `requests` library to get the text into Python. You can also save the file into the same folder as the `.py` file and open it using `with`.

```python
import requests
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)
```

We can also download a file of english words and place it next our `.py` file and load it like so:

```python
with open('the_raven.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)
```

Take the following steps to build up our dictionary. The result should look something like `{'a': 3, 'the': 4}`

1. Make everything lowercase,  strip punctuation, split into a list of words.
2. Your dictionary will have words as `keys` and counts as `values`. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
3. Print the most frequent top 10 out with their counts. You can do that with the code below.


```python
# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
```

## Version 2 (optional)

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

## Version 3 (optional)

Let the user enter a word, then show the words which most frequently follow it.
