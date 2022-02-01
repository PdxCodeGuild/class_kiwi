# Regular Expressions in Python

[Regular Expressions](../../0%20General/05%20Regular%20Expressions.md) are a way of matching patterns in text, they can be used for searching, doing input validation, and more. You can find out more about regular expressions in Python [here](https://docs.python.org/3.8/howto/regex.html#regex-howto) and [here](https://docs.python.org/3.8/library/re.html#re-syntax).

- [Raw Strings: `r''`](#raw-strings-r)
- [Match and Search: `re.match(pattern, text)`, `re.search(pattern, text)`](#match-and-search-rematchpattern-text-researchpattern-text)
- [Splitting: `re.split(pattern, text)`](#splitting-resplitpattern-text)
- [Find All: `re.findall(pattern, text)`](#find-all-refindallpattern-text)
- [Flags](#flags)
- [Compiling Regular Expressions](#compiling-regular-expressions)


## Raw Strings: `r''`

When writing regular expressions in Python as string literals, you should put an `r` before your string literal, so you can more easily write and read backslashes.

```python
s1 = 'we can\'t write \\ as easily, but escapes \' work'
s2 = r'we can write \ more easily, but escapes \" dont work'
print(s1) # we can't write \ as easily, but escapes ' work
print(s2) # we can write \ more easily but escapes \" dont work
```

## Match and Search: `re.match(pattern, text)`, `re.search(pattern, text)`

The `match` function is used to check that a string matches a pattern, starting from the beginning from the string. The `search` function behaves similarly, but will look for a match anywhere in the string.

```python
import re
print(re.match('a', 'abcdef'))    # match
print(re.match('c', 'abcdef'))    # no match
print(re.search('c', 'abcdef'))   # match
print(re.search('^c', 'abcdef'))  # no match
print(re.search('^a', 'abcdef'))  # match
```

If the pattern is matched, we'll get a match object in response.

```python
import re
result = re.match(r'\d{3}-\d{3}-\d{4}', '012-345-6789')
print(result) # <re.Match object; span=(0, 12), match='012-345-6789'>
```

We can then use methods on that object to get information about the match.

- `start()` returns the start of the match
- `end()` returns the end of the match
- `group()` and `group(0)` return the full match
- `group(1)`, `group(2)`, etc return the capture groups in order from left to right


```python
import re
result = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(result.group())      # The entire match 'Isaac Newton'
print(result.group(1))     # The first parenthesized subgroup 'Isaac'
print(result.group(2))     # The second parenthesized subgroup 'Newton'
print(result.group(1, 2))  # Multiple arguments give us a tuple ('Isaac', 'Newton')

result = re.match(r"([a-zA-Z]+) (\d+)", "June 14")
print(result.start()) # the beginning of the match, 0
print(result.end()) # the end of the match, 7
print(result.group()) # same as result.group(0), 'June 14'
print(result.group(1)) # 'June'
print(result.group(2)) # '24'
```

If the pattern isn't found, the result will be `None`, allowing us to use these functions in an `if` clause.

```python
import re
regex = r"([a-zA-Z]+) (\d+)"
if re.match(regex, "June 24"):
    ...
```

## Splitting: `re.split(pattern, text)`

The `split` function works just like it does with strings, but allows for regular expressions.

```python
import re
s = "Hello! Is this a question? This is a statement."
print(re.split('[.?!]', s)) # ['Hello', ' Is this a question', ' This is a statement', '']
```

## Find All: `re.findall(pattern, text)`

The `findall` function will return a list of strings containing all the matches.

```python
import re
results = re.findall(r'\d\d', '56-hi 41 hello 15 test67')
print(results) # ['56', '41', '15', '67']
```

If used with capture groups, it will return a list of tuples.

```python
import re
results = re.findall(r'(\d)(\d)', '56-hi 41 hello 15 test67')
print(results) # [('5', '6'), ('4', '1'), ('1', '5'), ('6', '7')]
```

## Flags

Flags allow us to control how regular expressions are applied. [examples](http://xahlee.info/python/python_regex_flags.html)

| short name | long name | meaning |
| --- | --- | --- |
| re.I | re.IGNORECASE | ignore case. |
| re.M | re.MULTILINE | make begin/end {^, $} consider each line. |
| re.S | re.DOTALL | make . match newline too. |
| re.U | re.UNICODE | make {\w, \W, \b, \B} follow Unicode rules. |
| re.L | re.LOCALE | make {\w, \W, \b, \B} follow locale. |
| re.X | re.VERBOSE | allow comment in regex. |


## Compiling Regular Expressions

The `compile` function allows us to 'compile' a regular expression into a regex object, which we can then call methods on.

```python
import re
reg_exp = re.compile(r'Hello, (\w+)', re.I)
match = reg_exp.search('Why hello, Alice.')
print(match) # <re.Match object; span=(4, 16), match='hello, Alice'>
```





