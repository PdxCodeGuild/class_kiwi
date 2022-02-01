
# Lists and Tuples

- [Defining Lists](#defining-lists)
- [List Operations](#list-operations)
  - [Access: `mylist[i]`](#access-mylisti)
  - [Assignment `mylist[index] = value`](#assignment-mylistindex--value)
  - [Length `len(mylist)`](#length-lenmylist)
  - [Comparison `mylist == otherlist`, `mylist != otherlist`](#comparison-mylist--otherlist-mylist--otherlist)
  - [Inclusion: `element in mylist`](#inclusion-element-in-mylist)
  - [Append: `mylist.append(element)`](#append-mylistappendelement)
  - [Insert: `mylist.insert(index, element)`](#insert-mylistinsertindex-element)
  - [Remove: `mylist.remove(element)`](#remove-mylistremoveelement)
  - [Pop: `mylist.pop(index)`](#pop-mylistpopindex)
  - [Delete `del mylist[index]`](#delete-del-mylistindex)
  - [Extend: `mylist.extend(otherlist)`](#extend-mylistextendotherlist)
  - [Copy: `mylist.copy()`](#copy-mylistcopy)
  - [Index: `mylist.index(element)`](#index-mylistindexelement)
  - [Slicing: `mylist[start : end : increment]`](#slicing-myliststart--end--increment)
  - [Reverse: `mylist.reverse()`](#reverse-mylistreverse)
  - [Sort: `mylist.sort()`](#sort-mylistsort)
  - [Built-in Functions `reversed` and `sorted`](#built-in-functions-reversed-and-sorted)
- [List Comprehensions](#list-comprehensions)
  - [Transforming Elements](#transforming-elements)
  - [Filtering Elements](#filtering-elements)
  - [Nested Comprehensions](#nested-comprehensions)
- [Tuples](#tuples)

## Defining Lists

Lists are collections of ordered elements. We can define lists using square brackets and commas. The elements a list contains don't have to all be of the same type.

```python
fruits = ['apple', 'banana', 'peach', 'pear']
nums = [4, 56, 73, 12]
mixed = [3, 'red', 45.012, [3, 5]] # lists can even contain other lists!
```


## List Operations


### Access: `mylist[i]`

Access list elements by index, note that indices start at 0. You can also access elements using negative indices, which begin from the end and go backward. Using an index which is beyond the list will cause an **IndexError**.

```python
#            0          1         2          3
fruits = ['apples', 'bananas', 'pears', 'cherries']
print(fruits[0]) # apples
print(fruits[2]) # pears
print(fruits[-1]) # cherries
print(fruits[-3]) # bananas
print(fruits[4]) # IndexError
```

### Assignment `mylist[index] = value`

```python
#            0          1         2
fruits = ['apples', 'bananas', 'pears']
fruits[0] = 'cherries'
print(fruits) # ['cherries', 'bananas', 'pears']
```


### Length `len(mylist)`

We can use the `len` function to get the length of a list:

```python
fruits = ['apple', 'banana', 'peach', 'pear']
print(len(fruits)) # 4
```

### Comparison `mylist == otherlist`, `mylist != otherlist`

We can use `==` and `!=` with lists.

```python
fruits1 = ['apples', 'bananas']
fruits2 = ['pears', 'cherries']
print(fruits1 == fruits2) # False
print(fruits1 != fruits2) # True
```

### Inclusion: `element in mylist`

We can check if a list contains an element using `in`.

```python
fruits = ['apples', 'bananas', 'pears']
if 'apples' in fruits:
    print('true!')
```
> true!

### Append: `mylist.append(element)`

We can use the `append` method to add an element to the end of a list.

```python
fruits = ['apple', 'banana', 'peach', 'pear']
fruits.append('pineapple')
print(fruits) # ['apple', 'banana', 'peach', 'pear', 'pineapple']
```

### Insert: `mylist.insert(index, element)`

We can insert an element into an arbitrary place in the list

```python
fruits = ['apples', 'bananas', 'pears']
fruits.insert(1, 'cherries') # insert an element at index 1
print(fruits) # ['apples', 'cherries', 'bananas', 'pears']
```

### Remove: `mylist.remove(element)`

We can use the `remove` method to remove an element. This only removes the first occurance.

```python
fruits = ['apples', 'pears', 'bananas', 'pears']
fruits.remove('pears')
print(fruits) # ['apples', 'bananas', 'pears']
```

### Pop: `mylist.pop(index)`

The `pop` method removes an element at a given index and returns it.

```python
fruits = ['apples', 'bananas', 'pears']
print(fruits.pop(1)) # 'bananas'
print(fruits) # ['apples', 'pears']
```

### Delete `del mylist[index]`

We can use the `del` operator to remove an element.

```python
fruits = ['apples', 'bananas', 'pears']
del fruits[1]
print(fruits) # ['apples', 'pears']
```

### Extend: `mylist.extend(otherlist)`

The `extend` method appends all the elements from one list to another.

```python
fruits1 = ['apples', 'bananas', 'pears']
fruits2 = ['cherries', 'pineapples']
fruits1.extend(fruits2) # ['apples', 'bananas', 'pears', 'cherries', 'pineapples']
print(fruits1)
```

### Copy: `mylist.copy()`

We can use the `copy` method to create a copy of a list. Editing a copy won't change the original.

```python
fruits1 = ['apples', 'bananas', 'pears']
fruits2 = fruits1.copy()
fruits2[0] = 'pineapples'
print(fruits1) # ['apples', 'bananas', 'pears']
print(fruits2) # ['pineapples', 'bananas', 'pears']
```


### Index: `mylist.index(element)`

The `index` method gives us the index of the first occurrence of an element.

```python
fruits = ['apples', 'bananas', 'pears']
print(fruits.index('bananas')) # 1
```

### Slicing: `mylist[start : end : increment]`

We can get sublists using square brackets and colons `[::]`, this is called slicing. The first number is the starting index, the second is the ending index, and the third is the increment. If you leave out the first number, it's implied to be the beginning. If you leave out the second number it's implied to be the end. If you leave out the third number, it's implied to be 1.

```python
nums = [4, 56, 73, 12, 17, 99, 42, 87]
print(nums) # [4, 56, 73, 12, 17, 99, 42, 87]
print(nums[2::]) # [73, 12, 17, 99, 42, 87]
print(nums[:2:]) # [4, 56]
print(nums[::-1]) # [87, 42, 99, 17, 12, 73, 56, 4]
print(nums[2:4:]) # [73, 12]
print(nums[:6:-1]) # [87]
print(nums[2:6:-1]) # []
print(nums[::-2]) # [87, 99, 12, 56]
```

### Reverse: `mylist.reverse()`

We can use the `reverse` method to reverse a list:

```python
fruits = ['apples', 'bananas', 'pears']
fruits.reverse()
print(fruits) # ['pears', 'bananas', 'apples']
```

### Sort: `mylist.sort()`

We can use the `sort` method to sort a list:

```python
fruits = ['cherries', 'bananas', 'pears', 'apples']
fruits.sort()
print(fruits) # ['apples', 'bananas', 'cherries', 'pears']
```

### Built-in Functions `reversed` and `sorted`

- `reversed(seq)` returns a reversed object when given an iterable, should be typecasted to list for further usage
- `sorted(seq)` returns a new sorted list when given an unsorted iterable, unlike `reversed(seq)` it does not need typecasting

```python
mystring = 'Python'
print(reversed(mystring)) # <reversed object at 0x7fb67b77dd68>
print(list(reversed(mystring))) # ['n', 'o', 'h', 't', 'y', 'P']
print(sorted(mystring)) # ['P', 'h', 'n', 'o', 't', 'y']
```

## List Comprehensions

List comprehensions allow us to generate a list with a single statement.

```python
nums = [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

This is equivalent to a loop with `append`.
```python
nums = []
for x in range(10):
    nums.append(x**2)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Transforming Elements

```python
names = ['David', 'Helen', 'Anne']
lower_names = [name.lower() for name in names]
lower_names  #> ['david', 'helen', 'anne']
```

```python
def lookup_phone_number_by_name(name):
    """Return the phone number of a person."""
    ...
names = ['David', 'Helen', 'Anne']
phone_numbers = [lookup_phone_number_by_name(name) for name in names]
```

### Filtering Elements

We can also put an `if` clause at the end of our comprehension to filter elements. The example below filters out leap years.

```python
people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
bobs_only = [person for person in people if person.startswith('Bob')]
```
> ['Bob J.', 'Bob F']

As another example, say we wanted to make a list of doubled odd elements. We could write it as...

```python
numbers = [1, 2, 3, 4, 5]
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
```

A more succinct way to write this is by using a comprehension.

```python
numbers = [1, 2, 3, 4, 5]
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
```

### Nested Comprehensions

```python
[[1 if col == row else 0 for col in range(0, 3)] for row in range(0, 3)]
```
> [[1, 0, 0],<br>
>  [0, 1, 0],<br>
>  [0, 0, 1]]<br>

## Tuples

**Tuples** are like lists, but immutable. Their literals are surrounded by parentheses `()`. For more info, check out the [official docs](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

Single item tuples need a trailing comma to distinguish them from grouping parentheses. Empty tuples are created using `tuple()`.

```python
('David', '503-555-9895')
(2016, 7, 13)
('Alice', )
tuple()
```

Why use tuples over lists? Lists tend to be used for _homogenous_ data, tuples tend to be used for "pairs", "triplets" or "n-tuples"; groupings of _heterogenous_ data. For example, a list of friends is a list because it doesn't matter exactly how many there are and all are names. A pair of address and phone number would be a tuple, since each is interpreted differently and if there was another item, it you wouldn't know what to do with it.

```python
friend_names = ['Kate', 'Al']
contact_info = ('123 Main St', '503-555-1234')
```

You can cast a sequence to a tuple with the `tuple()` function.

```python
fruits = ['apples', 'bananas', 'pears']
fruits_tuple = tuple(fruits)
print(fruits_tuple)
```

Tuples are immutable. Trying to modify them is an exception.

```python
contact_info = ('123 Main St', '503-555-1234')
contact_info[0] = '456 Water Ave'  # Throws TypeError
```

Also, realize there are four different ways to use parentheses now:

1. Order of operations
2. Line continuations
3. Function calls
4. Tuple literals

```python
x = (4 + 3) * 6
x = (4 *
     3 *
     8)
min(5, 6)
('Al', 'Kate')
```
You can also 'pack' a tuple into an other variable, and 'unpack' it into an other set of variables.
```python
x = ("Mr. Python", 30, "Java(script)")    # tuple packing
(name, age, fav_drink) = x    # tuple unpacking
print(name)
print(age)
print(fav_drink)

>>> Mr. Python
>>> 30
>>> Java(script)
```
