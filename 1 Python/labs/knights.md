# Lab: Knights who say Ni!

###### Delivery Method: Instructional exercise.

------------------------------

##### Goal

Learn how to write and execute a doctest.

---------------------------------------------------------

##### Instructions

  In short, doctests are comments that execute as code.

  A doctest can be used in testing that a function will return the correct result from calling zero or more inputs. It is written in the header of either the file or the function. It uses a very simple syntax of `>>> function(input0)` for what will be input, and the next line tests for the 'expected output' or 'assertion' from the given input.

  The best part: doctests invoke the functions for you, *so you don't have to.*

  This is the doctest you'll be using today:

```
>>> knights()
'Knights who say Ni!'
```

1. Define a function named knights() that returns a string to make the doctest pass.
2. See the doc test above. It is indicated by the `>>>`:
3. To run the doctest, checking if the function passes:
  - go to the directory of the file in your terminal.
  - Enter `$ python -m doctest knights.py`
  - Have a good 'Hurrah!' once you pass your doctest!


------------------

#### Documentation

* [Python Official Docs: doctests](https://docs.python.org/3.6/library/doctest.html)


------------------

#### Key Concepts

- Executing a doctest
