
# Loops

- [While Loops](#while-loops)
- [For-Loops](#for-loops)
  - [Range](#range)
  - [Strings](#strings)
  - [Lists](#lists)
- [Break and Continue](#break-and-continue)
  - [Break](#break)
  - [Continue](#continue)


## While Loops

`while` loops execute a block of code while a condition is true. Here, each iteration the value of `i` will increase by `1` until the value `i < 10` becomes false, and the loop will terminate.

```python
i = 0
while i < 5:
    print(i)
    i += 1
print('done')
```
> 0<br>
> 1<br>
> 2<br>
> 3<br>
> 4<br>
> done

You can add an `else` statement to a while loop. whatever is in the else statement will execute when the while loop is finished, but won't execute when you `break` out of one or if an exception is raised.
```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('done')
```
> 0
> 1
> 2
> 3
> 4
> done


## For-Loops


For-Loops are much more flexible, they allow us to iterate anything that's **iterable**: ranges, lists, strings, sets, dicts, etc. For loops in python are more like For-Each Loops in other languages. The table below shows each types of variables you'll get when writing `for x in y`

| x | y |
|--- |--- |
| int | range |
| char | string |
| element | list |
| element | tuple |
| element | set |
| key | dict |

### Range

To loop over a range of numbers, we can use `range`. The values it generates go up to but not including the number passed as a parameter (here, 10). Each iteration, the variable `i` will be bound to the values of `range`.

```python
>>> for i in range(10):
>>>     print(i, end=' ')
0 1 2 3 4 5 6 7 8 9
```

There are two other ways to use range. If you pass two paramaters, they'll represent the lower-bound and upper-bound.

```python
>>> for i in range(4, 10):
>>>     print(i, end=' ')
4 5 6 7 8 9
```

If you pass 3 numbers, the first is the lower-bound, the second is the upper-bound, and the third is the **increment**.

```python
>>> for i in range(4, 10, 2):
>>>     print(i, end=' ')
4 6 8
``` 

Thus passing 1 parameter to range is equivalent to having the lower bound at 0, and the increment at 1.

```python
 # these two are equivalent
for i in range(10):
    ...
for i in range(0, 10, 1):
    ...
```

### Strings

You can use a for loop with a string to iterate over its characters one at a time.

```python
text = 'hello!'
for char in text:
    print(char) 
```
> h<br>
> e<br>
> l<br>
> l<br>
> o<br>
> !



### Lists

If we use a list, we can iterate over the elements.
```python
fruits = ['apples', 'bananas', 'pears']
for fruit in fruits:
    print(fruit)
```
> apples
> bananas
> pears

We can also iterate over the indices by using a `range`.

```python
fruits = ['apples', 'bananas', 'pears']
for i in range(len(fruits)):
    print(str(i) + ' ' + fruits[i])
```
> 0 apples
> 1 bananas
> 2 pears

If we want both the indices and values at the same time, we can use enumerate. This uses tuple unpacking.

```python
fruits = ['apples', 'bananas', 'pears']
for i, fruit in enumerate(fruits):
    print(str(i) + ' ' + fruit)
```
> 0 apples
> 1 bananas
> 2 pears


## Break and Continue

The keywords `break` and `continue` are two ways of controlling the operation of a loop.

### Break

`break` causes the loop to exit immediately, not executing any more statements of the loop's body.

```python
for i in range(100):
    print(i, end=' ')
    if i == 5:
        break
```
> 0 1 2 3 4 5

This is particularly useful when you need tighter control over when a loop terminates, and can use an infinite loop (`while True`) with a `break`.

```python
nums = []
while True:
    num = input('enter number: ')
    if num == 'done':
        break
    nums.append(int(num))
print(nums)
```

It only works on the loop that you're currently in however, not the loop that loop is in if you're using nested loops.

```python
nums = [1,2,3,4]
while True:
    for num in nums:
        print(num, end=' ')
        if num == 3:
            break
```
> 1 2 3 1 2 3 1 2 ...

### Continue

The `continue` statement skips the current iteration and continues with the next. Any code after `continue` is hit will not be run. In the example below, we skip iterations that are of odd numbers.

```python
for i in range(20):
    if i%2 == 1:
        continue
    print(i, end=' ')
```
> 0 2 4 6 8 10 12 14 16 18

