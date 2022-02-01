# The Random Module

## Random Element: `random.choice(x)`

The `random.choice(x)` function returns a random element of a list, or a random character of a string.

```python
import random
print(random.choice(['apples', 'bananas', 'pears'])) # randomly prints apples, bananas, or pears
print(random.choice('abc')) # randomly prints a, b, or c
```

## Random Integer: `random.randint(x, y)`

The `random.randint(x, y)` function returns a random integer between `x` and `y` (inclusive - it can be `x` or `y` as well).

```python
import random
print(random.randint(5, 10)) # randomly prints 5, 6, 7, 8, 9, or 10
```

## Shuffle: `random.shuffle(x)`

The `random.shuffle(x)` module randomly shuffles a list in-place (it does not return a new list).

```python
import random
fruits = ['apples', 'bananas', 'pears']
random.shuffle(fruits)
print(fruits) # e.g. ['bananas', 'pears', 'apples']
```