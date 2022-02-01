
# Booleans, Comparisons, and Conditionals

- [Booleans](#booleans)
  - [And: `and`](#and-and)
  - [Or: `or`](#or-or)
  - [Not: `not`](#not-not)
- [Comparisons](#comparisons)
  - [Shorthand: `a < b < c`](#shorthand-a--b--c)
  - [Shorthand: `a == b == c`](#shorthand-a--b--c-1)
  - [`in`, `not in`](#in-not-in)
  - [`is`, `is not`](#is-is-not)
- [Conditionals: `if` `elif` `else`](#conditionals-if-elif-else)
  - [Short-Circuited Evaluation](#short-circuited-evaluation)
  - [Shorthand: `x if c else y`](#shorthand-x-if-c-else-y)
  - [Truthy and Falsey](#truthy-and-falsey)

## Booleans

Booleans are one of the built-in types, and represent either `True` or `False`. There are three boolean operators: `not`, `and` and `or`.


| `a` | `b` | `a and b` | `a or b` |  `not a` |
| --- | --- | ---       | ---      | ---      |
| F   | F   | F         | F        | T        |
| F   | T   | F         | T        | T        |
| T   | F   | F         | T        | F        |
| T   | T   | T         | T        | F        |



### And: `and`

`a and b` is true if `a` is true and `b` is true

```python
print(False and False) # False
print(True and False) # False
print(False and True) # False
print(True and True) # True
```

### Or: `or`

`a or b` is true if `a` is true or `b` is true

```python
print(False or False) # False
print(True or False) # True
print(False or True) # True
print(True or True) # True
```

### Not: `not`

`not a` will be the opposite of a

```python
print(not True) # False
print(not False) # True
```

## Comparisons

Comparisons will resolve to a `True` or `False` value.

- `==` equals
- `!=` not-equals
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to


### Shorthand: `a < b < c`

If you're comparing whether a value is between two other values, you can also write it without an `and`: `x > 5 and x < 10` can also be written as `5 < x < 10`. It can not be written as `x < 5 and > 0`, Python won't know what to do with that statement and will give you a `Syntax Error`.


### Shorthand: `a == b == c`

Python also allows comparing multiple values at once. Realize though that `5==5==5` is not the same thing as `(5==5)==5`. This is because in the first case it makes the comparison between the first `5==5` and the second `5==5` which both return `True` making the overall statement true. In the second case it makes the `(5==5)` comparison, which returns `True` and then compares that `True` to `5`, which returns `False` since `5` does not equal `True`.

```python
print(5==5==5) # True
print((5==5)==5) # False
```

### `in`, `not in`

The `in` operator can be used to see if a element is in a list or not:

```python
my_list = [1,2,3,4,5]
x = 3
y = 6
print(x in my_list) # True
print(y in my_list) # False
print(y not in my_list) # True
```

### `is`, `is not`

The `is` operator is used to see if two variables point to the same `Object` or not. Note, however, that if you assign two variables the same value then python will sometimes try to make them point to the same object to save memory. As a general rule it's better practice to use `==` when comparing number values or objects.

```python
x = 5
y = 5
my_list1 = [5, 4, 3, 2, 1]
my_list2 = [5, 4, 3, 2, 1]
print(x is y) # True
print(my_list1 is my_list2) # False
print(my_list1 == my_list2) # True
```

## Conditionals: `if` `elif` `else`

Conditionals allow you to have different collections of code execute if a condition is true or false. These include `if`, `elif`, and `else`. You can chain these in several ways. You must start with an `if`, followed by zero or more `elif`s, followed by zero or one `else`.

- if
- if-else
- if-elif
- if-elif-else
- if-elif-elif-elif-...-else


The body which executes will be the first whose condition matches, or `else` if none of them match. Only one body of an if-elif-chain will execute, they're mutually exclusive. Therefore, it's unnecessary to rule-out prior conditions.

```python
temperature = 45

if temperature < 60:
    print('cold')
elif temperature >= 60 and temperature < 70:
    print('warm')

 # can be re-written as...

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
```
You can have as many `elif`'s as you want, but only one `else`. `elif`'s can follow an `if` or an other `elif`. `else`'s can also only follow an `if` or `elif`.
```python
if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
elif temperature < 80:
    print('pretty warm')
elif temperature < 90:
    print('hot')
else:
    print("wow it's so hot!")
```

### Short-Circuited Evaluation

Python (and Javascript which will be covered later) make short-circuited evaluations with `or` and `and`. This means that for an `or` if the first argument happens to be true then it will just continue the code instead of checking the second argument. Vice-versa, for an `and` if the first argument is false the comparison will short circuit and continue the code instead of checking the other argument. This is because `True or False` wil always be `True`, and `False and True` will always be `False`. Note that written the other way, `False or True`, the first argument will return `False` but because there is an or it will need to check to see if the second argument is `True` or not before being able to evaluate whether the whole statement is `True` or `False`. The same holds true for `True and False`.

This is useful if you want to check if something exists before trying to access some data on it. Here, `len(nums)` would raise an exception if `nums` was `None` and we didn't have short-circuited evaluation.

```python
def has_elements(nums):
    return nums is not None and len(nums) > 0
print(has_elements(None)) # False
print(has_elements([])) # False
```


### Shorthand: `x if c else y`

It's possible to write a conditional on one line, as `x if condition else y`. For example, a `min` function might be written as

```python
def min(a, b):
    return a if a < b else b
print(min(5, 2)) # 2
```

Because you can return boolean values from functions, you can also use a function in an `if` or `elif`.

```python
def bigger_than_five(x):
    return x > 5
y = 5
if bigger_than_five(y):
    print("its bigger")
else:
    print("not bigger")
```
> not bigger

### Truthy and Falsey

Python will also check to see if a statement is "truthy" or "falsey". This is generally name used to see if a statement is empty or not. However `True` or `False` is never written and instead the check is simply made against the variable itself. You can read more about truthy and falsey [here](https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-in-python-how-is-it-different-from-true-and-false).

```python
values = [0, 1, '', 'hi', [], ['hi'], {}, {'a':1}]
for value in values:
    print(value, 'is', end=' ')
    if value:
        print('truthy')
    else:
        print('falsey')
```
> 0 is falsey
> 1 is truthy
> is falsey
> hi is truthy
> [] is falsey
> ['hi'] is truthy
> {} is falsey
> {'a':1} is truthy



