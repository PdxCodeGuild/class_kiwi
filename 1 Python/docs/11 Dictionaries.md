# Dictionaries

**Dictionaries** or 'dicts'  provide an unordered, mutable, sequence of key-value pairs or a mapping between keys and values. For more information check the [official docs](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) and [w3schools](https://www.w3schools.com/python/python_dictionaries.asp). Keys have to be unique, values do not. Any _immutable_ value (int, float, string, tuple) can be a key, thus lists and other dicts can't be keys. Values can be any type.

- [Defining Dictionaries](#defining-dictionaries)
- [Accessing a Value with a Key: `dict[key]`](#accessing-a-value-with-a-key-dictkey)
- [Accessing a Value with a Key Safely: `dict.get(key)`](#accessing-a-value-with-a-key-safely-dictgetkey)
- [Updating a Key-Value Pair: `dict[key] = value`](#updating-a-key-value-pair-dictkey--value)
- [Adding a Key-Value Pair: `dict[key] = value`](#adding-a-key-value-pair-dictkey--value)
- [Removing a Key-Value Pair: `del dict[key]`](#removing-a-key-value-pair-del-dictkey)
- [Checking if a Key Exists: `key in dict`](#checking-if-a-key-exists-key-in-dict)
- [Combining Dictionaries: `dict1.update(dict2)`](#combining-dictionaries-dict1updatedict2)
- [Retrieving Keys and Values](#retrieving-keys-and-values)
- [Order](#order)
- [Conversions](#conversions)


## Defining Dictionaries

Dictionary literals are written using curly braces, and key-value pairs defined with colons and separated by commas.

```python
{'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
```

## Accessing a Value with a Key: `dict[key]`

The values of a dictionary are accessed by using the square-brackets with the **key**, similarly to how we access a specific element from a list using its **index**. If you use a key which does not exist in the dictionary, you'll get a **KeyError**.

```python
fruits = {'apple': 1.0, 'banana': 1.5, 'pear': 0.75}
print(fruits['apple'])  # 1.0
print(fruits['pear'])  # 0.75
print(fruits['grapes'])  # Throws KeyError
```


## Accessing a Value with a Key Safely: `dict.get(key)`

The `get` method allows us to safely access a value with a key. If the key is not in the dictionary, it will return `None`. You can also specify a second parameter as a default, which will be returned if the result is not found.


```python
fruits = {'apple': 1.0, 'banana': 1.5, 'pear': 0.75}
print(fruits.get('apple'))  # 1.0
print(fruits.get('grapes'))  # None
print(fruits.get('grapes', 4.0)) # 4.0
```

## Updating a Key-Value Pair: `dict[key] = value`

Values can then be added or updated by using the assignment operator `=`.

```python
fruits = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
fruits['apple'] = 2.0
fruits['pear'] += 0.5
print(fruits)  # {'apple': 2.0, 'pear': 2.0, 'grapes': 0.75}
```


## Adding a Key-Value Pair: `dict[key] = value`

```python
fruits = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
fruits['banana'] = 0.25
print(fruits) # {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

## Removing a Key-Value Pair: `del dict[key]`

You can delete a key-value pair using the `del` operator.

```python
fruits = {'apple': 1.0, 'banana': 1.5, 'pear': 0.75}
del fruits['apple']
print(fruits) # {'banana': 1.5, 'pear': 0.75}
```

## Checking if a Key Exists: `key in dict`

To check if a dictionary contains a key, use `in`

```python
fruits = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
if 'apple' in fruits:
    print('apple ' + str(fruits['apple'])) # 'apple 1.0'
```

## Combining Dictionaries: `dict1.update(dict2)`

To combine two dictionaries, use the `.update()` type method. Note that it changes the given dict and does not return a new one.

```python
fruits = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
fruits.update({'banana': 0.25})
fruits  #> {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

## Retrieving Keys and Values

There are a few type methods that allow you to view different parts of the dictionary. All produce sequences and not proper lists, so cast them to a list to use them normally.

```python
list(fruits.keys())  #> ['pear', 'apple', 'grapes']
list(fruits.values())  #> [0.75, 1.0, 1.5]
list(fruits.items())  #> [('grapes', 0.75), ('apple', 1.0), ('pear', 1.5)]
```

## Order

Dictionaries are unordered; there is no guarantee the same order will come out at each call. Call `sorted()` on the results if you need a stable order.

```python
sorted(fruits.keys())  #> ['apple', 'grapes', 'pear']
```

## Conversions

You can cast a sequences of two-tuples to a dictionary using `dict()`. This means `.items()` and `dict()` are inverses.

```python
names_and_fav_colors = [('Alice', 'red'), ('David', 'green')]
print(dict(names_and_fav_colors))  #> {'Alice': 'red', 'David': 'green'}
dict(names_and_fav_colors.items()) == names_and_fav_colors  #> True
```

# Dict Comprehensions

Dict comprehensions also look similar to list comprehensions, but with curly braces and colons.

```py
names_to_ages = {'Amanda': 90, 'David': 50}
names_to_ages = {name: age / 2 for name, age in names_to_ages.items()}
print(names_to_ages) # {'Amanda': 45, 'David': 25}
```
