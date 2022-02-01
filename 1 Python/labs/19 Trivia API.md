

# Trivia API

Let's use the [Open Trivia Database API](https://opentdb.com/api_config.php) to a write a quiz program.

## Part 1

Send a request to the following url: `https://opentdb.com/api.php?amount=10&category=18&type=boolean`. This will return a list of 10 true/false computer questions. Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

Certain characters in the question text are [encoded](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#Character_references), to decode them you'll have to use the `html` module's `unescape` method.

```python
import html
print(html.unescape('&quot;hello&amp;world&quot;')) # "hello&world"
```


## Part 2 (optional)

The API has many more options for different difficulties, different categories, and both true/false and multiple choice questions. Below are list of dictionaries containing the parameter name (what gets put into the query string) and a friendly name to show the user. Prompt the user for each of these parameters, and include them in the request to get the list of questions. Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

```python
difficulties = [
    { 'parameter': 'any', 'name': 'Any Difficulty'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]

types = [
    { 'parameter': 'any', 'name': 'Any Type'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]

categories = [
    { 'parameter': 'any', 'name': 'Any Category' },
    { 'parameter': '9', 'name': 'General Knowledge' },
    { 'parameter': '10', 'name': 'Entertainment: Books' },
    { 'parameter': '11', 'name': 'Entertainment: Film' },
    { 'parameter': '12', 'name': 'Entertainment: Music' },
    { 'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres' },
    { 'parameter': '14', 'name': 'Entertainment: Television' },
    { 'parameter': '15', 'name': 'Entertainment: Video Games' },
    { 'parameter': '16', 'name': 'Entertainment: Board Games' },
    { 'parameter': '17', 'name': 'Science &amp; Nature' },
    { 'parameter': '18', 'name': 'Science: Computers' },
    { 'parameter': '19', 'name': 'Science: Mathematics' },
    { 'parameter': '20', 'name': 'Mythology' },
    { 'parameter': '21', 'name': 'Sports' },
    { 'parameter': '22', 'name': 'Geography' },
    { 'parameter': '23', 'name': 'History' },
    { 'parameter': '24', 'name': 'Politics' },
    { 'parameter': '25', 'name': 'Art' },
    { 'parameter': '26', 'name': 'Celebrities' },
    { 'parameter': '27', 'name': 'Animals' },
    { 'parameter': '28', 'name': 'Vehicles' },
    { 'parameter': '29', 'name': 'Entertainment: Comics' },
    { 'parameter': '30', 'name': 'Science: Gadgets' },
    { 'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga' },
    { 'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations' }
]
```



