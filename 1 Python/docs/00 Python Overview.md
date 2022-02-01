
# Overview
- [Running Python](#running-python)
- [Installing Packages with `pip`](#installing-packages-with-pip)
- [Checking Your Installation Path](#checking-your-installation-path)
- [Common Built-in Modules](#common-built-in-modules)
- [Other Popular Modules](#other-popular-modules)
- [Keywords](#keywords)
- [Resources](#resources)
  - [Practice Problems](#practice-problems)
  - [Courses / Online Books](#courses--online-books)
  - [Lists of Resources](#lists-of-resources)
  - [Online Courses](#online-courses)
  - [Books](#books)
  - [Reference Documents and Tutorials](#reference-documents-and-tutorials)

Python is a popular general-purpose multi-paradigm programming language. General purpose means it can be used for a variety of purposes: desktop applications, [games](https://wiki.python.org/moin/GameProgramming), [embedded systems](https://micropython.org/), web development (Flask and Django), [data science](https://www.upwork.com/hiring/data/15-python-libraries-data-science/), [artificial intelligence](https://wiki.python.org/moin/PythonForArtificialIntelligence) and more. It also means that its core principles carry over to other languages, so you'll be able to more easily broaden your horizon. Python always has an active community with plenty of learning resources, conferences, and libraries. For more information, check out the [Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index) and [Python Standard Library](https://docs.python.org/3/library/index.html). The [wikipedia article](https://en.wikipedia.org/wiki/Python_(programming_language)) offers a decent overview.


## Running Python

The python interpreter is run through the terminal, and can be used interactively, or to run a `.py` file. You can find more info in the [official docs](https://docs.python.org/3/using/cmdline.html).


- `python` start the interactive interpreter, use `quit()` to close it
- `python <file>` execute the python source code in the given file
- `python <file> <arguments>` execute a python file and [pass arguments](https://docs.python.org/3/howto/argparse.html)
- `python --help` print out all command-line options
- `python --version` show which version of python you're using

## Installing Packages with `pip`

[Pip](https://pip.pypa.io/en/stable/) stands for 'pip installs python', and is used to manage packages.

- `pip install <package>` install a package
- `pip freeze` list installed packages
- `pip freeze > requirements.txt` save installed package names into a file
- `pip install -r requirements.txt` install packages from names in a file
- `pip uninstall <package>` uninstall a package


## Checking Your Installation Path

```python
import sys
print(sys.executable)
```

## Common Built-in Modules

- [math](https://docs.python.org/3/library/math.html) additional math functions like cos, sin, 
- [decimal](https://docs.python.org/3/library/decimal.html) more advanced floating point arithmetic
- [random](https://docs.python.org/3/library/random.html) generate random numbers
- [datetime](https://docs.python.org/3/library/datetime.html), [time](https://docs.python.org/3/library/time.html), [calendar](https://docs.python.org/3/library/calendar.html) working with dates and times
- [re](https://docs.python.org/3/library/re.html) regular expressions
- [os](https://docs.python.org/3/library/os.html) file operations
- [itertools](https://docs.python.org/3/library/itertools.html), [functools](https://docs.python.org/3/library/functools.html) advanced operations on iterables and functions
- [collections](https://docs.python.org/3/library/collections.html) data structures
- [csv](https://docs.python.org/3/library/csv.html) csv file parsing


## Other Popular Modules

These can be installed using `pip install <module>`. You can find more libraries [here](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/), [here](https://tryolabs.com/blog/2017/12/19/top-10-python-libraries-of-2017/), and [here](http://www.pythonforbeginners.com/api/list-of-python-apis)

- [pillow](https://python-pillow.org/): image manipulation
- [requests](http://requests.readthedocs.io/en/master/): http requests
- [twisted](http://twistedmatrix.com/trac/): networking engine
- [scrapy](https://scrapy.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): web scraping
- [nltk](http://www.nltk.org/): natural language processing
- [numPy](http://www.numpy.org/): advanced mathematics
- [scipy](https://www.scipy.org/): scientific computing
- [pygame](http://www.pygame.org/news.html): game framework
- [matplotlib](http://matplotlib.org/): 2D/3D plotting
- [tkinter](https://wiki.python.org/moin/TkInter), [wxPython](https://www.wxpython.org/), [PyQT](https://sourceforge.net/projects/pyqt/), [PyGTK](https://wiki.python.org/moin/PyGtk): GUI



## Keywords

```python
import keyword
keyword.kwlist
```
| keyword | description |
| ---     | --- |
| **and** | boolean operator |
| **as** | used with imports |
| **assert** | used for debugging |
| **async** | asynchronous |
| **await** | asynchronous |
| **break** | used with loops, exit the current loop |
| **class** | blueprints of an object, including data and methods |
| **continue** | used for loops, skip the rest of the current iteration and go to the next |
| **def** | define a function |
| **del** | delete, used with lists and dicts |
| **elif** | else-if, part of a conditional |
| **else** | part of a conditional |
| **except** | part of exception handling |
| **False** | boolean literal |
| **finally** |  part of exception handling |
| **for** | define a for-loop |
| **from** | used with imports |
| **global** | define a global variable |
| **if** | part of conditionals |
| **import** | used with imports |
| **in** | a boolean operator, also part of for-loops |
| **is** | a boolean operator, tests for equality |
| **lambda** | a short-hand function |
| **None** | represents the absence of a value |
| **nonlocal** | variable scope |
| **not** | a boolean operator |
| **or** | a boolean operator |
| **pass** | a placeholder |
| **raise** | exceptions |
| **return** | functions |
| **True** | boolean literal |
| **try** | exceptions |
| **while** | looping |
| **with** | safely open and close files |
| **yield** | generators |



## Resources

### Practice Problems

- [Codecademy - Python](https://www.codecademy.com/learn/learn-python-3)
- [codewars.com](https://www.codewars.com/?language=python)
- [CodingBat](https://codingbat.com/python)
- [Py](https://www.getpy.com/mobile): an app for Android and iOS
- [practicepython.org](http://www.practicepython.org/)
- [codingbat.com exercises](http://codingbat.com/python)
- [w3resource.com exercises](http://www.w3resource.com/python-exercises/)

### Courses / Online Books

- [thinkcspy](https://runestone.academy/runestone/books/published/thinkcspy/index.html)

### Lists of Resources

- [fullstackpython.com](https://www.fullstackpython.com/table-of-contents.html) has a list of [resources](https://www.fullstackpython.com/best-python-resources.html) and [videos](https://www.fullstackpython.com/best-python-videos.html)
- [python.berkeley.edu list](http://python.berkeley.edu/resources/)
- [wiki.python.org list](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- [hakin9.org list](https://hakin9.org/list-of-free-python-resources/)
- [stackoverflow.com blog post](https://stackoverflow.blog/2017/09/12/best-resources-learning-python-every-developer/)
- [some random guy's list](https://github.com/adrianmoisey/learn-python)


### Online Courses


- [learnpython.org](https://www.learnpython.org)
- [tutsplus.com](https://code.tutsplus.com/articles/the-best-way-to-learn-python--net-26288)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)
- [Google for Education - Python (2.7)](https://developers.google.com/edu/python/)
- [rmotr.com](https://rmotr.com/) (not free)
- [datacamp.com](https://www.datacamp.com/) (not free)

### Books

- [Think Python](http://greenteapress.com/thinkpython/html/index.html)
- [Dive Into Python 3](http://www.diveintopython3.net/)
- [A Byte of Python](https://python.swaroopch.com/)

### Reference Documents and Tutorials

- [Cheat Sheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html)
- [Official Docs](https://docs.python.org/3/)
- [w3resource.com tutorial](https://www.w3resource.com/python/python-tutorial.php)
- [Library of algorithms implemented in Python](https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md)

