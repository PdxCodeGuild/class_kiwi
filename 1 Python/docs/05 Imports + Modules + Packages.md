
# Modules and Packages

- [Modules](#modules)
  - [Importing a Module](#importing-a-module)
  - [Importing Parts of a Module](#importing-parts-of-a-module)
  - [Importing an Renaming](#importing-an-renaming)
  - [Main: `\_\_name__`](#main-__name__)
- [Packages](#packages)
  - [Relative Imports](#relative-imports)


## Modules

A module is one of the major organizational structures of a Python program. It allows you to encapsulate a collection of variables, function, and classes together to be re-used by other code. A module is defined by a file with the extension `py`.


### Importing a Module

**module1.py**
```python
x = 10
def add(a, b):
    return a + b
```

**module2.py**
```python
import module1
print(module1.x) # 10
print(module1.add(5, 2)) # 7
```


### Importing Parts of a Module

Writing the whole file name every time you'd like to use a function from it can be tedious though, so we can use `from` to make our lives easier.

**functions.py**
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

**test.py**
```python
from functions import add, subtract

print(add(5,4)) # 9
print(subtract(5,4)) # 1
```

### Importing an Renaming

We can use the `as` keyword to shorten it even further:

**test.py**
```python
from functions import add as a, subtract as s

print(a(5,4)) # 9
print(s(5,4)) # 1
```

Other imports:
```python
import x
from x import * #Imports everything from file
x = __import__('X')
```

### Main: `\_\_name__`

When a module is run directly or imported, a variable `__name__` is passed into it. If the module is run directly, `__name__` will be `'__main__'`, otherwise it will be the module name itself. This allows you to execute code only when a module is run directly, and not when it's imported into another file, which is useful for having test code inside the module.

For an example, check out the source code of [random.py](https://github.com/python/cpython/blob/3.8/Lib/random.py), which is the random module. Toward the bottom is an `if __name__ == '__main__':` containing some tests. If you run `python -m random` you'll see the output of these tests, but if you `import random` in another module, you won't.

In the example below, if you run `python module1.py` you'll see "5 + 2 = 7". If you run `python module2.py` you'll see "10" and "7".


In the exampl
**module1.py**
```python
x = 10

def add(a, b):
    return a + b

if __name__ == '__main__':
    # if this module is run directly, this code will run
    # if the module is imported into another, it won't run
    x = add(5, 2)
    print(f'5 + 2 = {x}')
```

**module2.py**
```python
import module1
print(module1.x) # 10
print(module1.add(5, 2)) # 7
```


## Packages

A package is another major unit of a Python program, and become important as a program grows in scale. A package is simply a collection of modules and other packages, and is represented by a folder several containing `.py` files. The folder must also contain a blank file with the name `__init__.py`. This allows for better organization of a large number of modules.

### Relative Imports

You can import across modules from packages using `.`. [Real Python](https://realpython.com/absolute-vs-relative-python-imports/)

```python
from package import module
from package.module import function
from package1.package2 import module
from ..pack
```


