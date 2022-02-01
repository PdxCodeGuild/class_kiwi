
# Regular Expressions

Regular expressions or 'regex' are a way to match patterns in strings. They can be executed in nearly any programming language. They can be used to validate a phone number or address in an input field on a website, or to find the occurrences of a phrase in a block of text, etc. There are also docs on [Regular Expressions in Python](../1%20Python/12%20-%20Regular%20Expressions%20in%20Python.md) and [Regular Expressions in JavaScript](../3%20JavaScript/Regex%20and%20Form%20Validation.md).

- [Resources](#resources)
- [Overview](#overview)
- [Character Match: `abc`](#character-match-abc)
- [Character Classes: `.`, `\d`, `\s`, `\w`](#character-classes--d-s-w)
- [Character Sets: `[]`](#character-sets-)
- [Repeats: `?`, `*`, `+`, `{}`](#repeats----)
- [Line Match: `^`, `$`](#line-match--)
- [Escapes: `\`](#escapes-)
- [Captures: `()`](#captures-)
- [Flags: `g`, `i`, `m`](#flags-g-i-m)
  - [Global: `g`](#global-g)
  - [Case-Insensitive: `i`](#case-insensitive-i)
  - [Multi-line: `m`](#multi-line-m)


## Resources

- [Regex101](https://regex101.com): Test regular expressions
- [RegexOne](https://regexone.com/): Learn regular expressions
- [RegexLib](https://regexlib.com/): A library of regular expressions
- [Regexr](https://regexr.com/): Test, Learn, & Share regular expressions

## Overview

- `abc123...` match a character literally
- `.` matches any character except a newline
- `\d` matches any digit character (0-9)
- `\s` matches any whitespace character (space, \t, or \n)
- `\w` matches any word character (A-Z, a-z, 0-9, and _)
- `[]` define a character class
- `^` matches the beginning of a line, within a character class it matches everything BUT what follows
- `$` matches the end of a string, or just before the next newline
- `*` matches 0 or more occurrences
- `+` matches 1 or more occurrences
- `?` matches 0 or 1 occurrences

## Character Match: `abc`

Most characters match themselves.

```re
david s
```
> **david s**<br/>
> David s<br/>
> hello **david s**<br/>
> hello **david s** today<br/>


## Character Classes: `.`, `\d`, `\s`, `\w`

Groups of characters that are used in the same sorts of ways are called **classes**.

We can use `.` to match any character.

```re
davi. s
```
> **david s**<br/>
> **davi1 s**<br/>
> **davi! s**<br/>
> davidd s


We can use `\d` to match digits.

```re
I ate \d apples
```
> **I ate 2 apples**<br/>
> **I ate 8 apples**<br/>
> I ate five apples


We can use `\s` to match white space (space, tab, newline)

```re
outer\sspace
```
> **outer space**<br/>
> **outer\tspace**<br/>
> outer3space


We can use `\w` to match "word" characters (letters, numbers, and underscore)


```re
\w
```
> **w**<br/>
> **5**<br/>
> **_**<br/>
> !



## Character Sets: `[]`

If you want to be more discerning than a whole character class, you can use a **set**. Put all the characters you want to allow in square brackets `[]`. Each set still only matches one character, but repeat characters can be used on them.

```re
[bp]anana
```
> **banana**<br/>
> **panana**<br/>
> pbanana


You can specify **ranges** of characters with dash `-`, so dash must be escaped in a character set. A super common range is all letters `[a-zA-Z]` since `\w` also includes digits.

```re
My Name Is: [a-zA-Z]+
```
> **My Name Is: David**<br/>
> My Name Is: C4t



## Repeats: `?`, `*`, `+`, `{}`

There are some special characters that mark how many times the previous character should repeat.

The `?` character means one or zero times.

```re
sna?cks
```
> **sncks**<br/>
> **snacks**<br/>
> snaaaaacks

The `+` character means one or more times.

```re
sna+cks
```
> sncks<br/>
> **snacks**<br/>
> **snaaaaacks**

The `*` character means zero or more times.

```re
sna*cks
```
> **sncks**<br/>
> **snacks**<br/>
> **snaaaaacks**

The `{}` characters can allow us to repeat a specific number of times.

```re
sna{5}ks
```
> sncks<br/>
> snacks<br/>
> **snaaaaacks**

Two numbers specify a lower and upper bound.

```re
sna{3,5}ks
```
> sncks<br/>
> snacks<br/>
> **snaaacks**<br/>
> **snaaaaacks**


## Line Match: `^`, `$`

- Carrot `^` matches the beginning of a line
- Dollar sign `$` matches the end of a line

```re
^fire
```
> **fire** hydrant<br/>
> no fire here<br/>

```re
fire$
```
> wood **fire**<br/>
> fire wood<br/>


## Escapes: `\`

If you want to use any special characters literally, use backslash `\` in front of it.

```re
Hello\.
```
> **Hello.**<br/>
> Hellox


## Captures: `()`

You can group together parts of a match into a **capture**, which is like a "sub-match", using parentheses `()`. You can then use the repeat modifiers on the whole capture.

More useful than that, is when the regular expression library matches text, it will save which parts of the text match each capture by the order they appear (1, 2, etc.). This is always one-indexed.

```re
(\d\d\d)-(\d\d\d)-(\d\d\d\d)
```
> **123-456-7890**

Instead of just remembering the text that matched each capture by the order it appears in the whole regular expression, you can also use a **named capture**. It is still a sub-match specified in parentheses `()`, but with `?P<NAME>` first inside.

```re
(?P<first_name>.+) (?P<last_name>.+)
```
> **bob dole**


## Flags: `g`, `i`, `m`

### Global: `g`

The `g` flag allows us to get multiple matches, rather than just one.

Without the `g` flag:
```re
hello
```
> **hello** goodbye
> goodbye hello

With the `g` flag:
```re
hello
```
> **hello** goodbye
> goodbye **hello**

### Case-Insensitive: `i`

The `i` flag allow us to make case insensitive matches.

Without the `i` flag:
```re
hello
```
> Hello

With the `i` flag:
```re
hello
```
> **Hello**

### Multi-line: `m`

The `m` flag makes `^` and `$` refer to the beginning and end of a line, rather than the whole string.

Without the `m` flag:
```re
^hello
```
> **hello** goodbye
> goodbye hello
> hello goodbye

With the `m` flag:
```re
^hello
```
> **hello** goodbye
> goodbye hello
> **hello** goodbye