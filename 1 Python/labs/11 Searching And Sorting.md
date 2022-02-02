# Lab 11: Searching and Sorting


[Big-O Notation](https://en.wikipedia.org/wiki/Big_O_notation) is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. For example, performing a linear search on a list of `n` elements takes, on average, `n/2` steps, so we say a linear search is `O(n)`. We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

## Part 1 - Linear Search

Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.

Example run:
```
 I
[1, 2, 3, 4, 5, 6, 7, 8]
    I
[1, 2, 3, 4, 5, 6, 7, 8]
       I
[1, 2, 3, 4, 5, 6, 7, 8]
```

Stub:
```python
def linear_search(nums, value):
  ...
# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
```

## Part 2 - Binary Search

Implement [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm), which requires that a list is sorted and divides its search range in half each iteration until it finds its target.
- Begin by defining two indices: `low` and `high`. Initialize `low` as the lowest index in the list and `high` as the highest.
- Loop while `low` is less then `high`.
  - For each iteration, calculate a third index `mid` which is in the middle between `low` and `high`
  - If the element at `mid` is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at `mid`. If it's less, make `high` equal to `mid` and loop.
  - If it's greater, make `low` equal to `mid` and loop. If the loop terminates without returning, return a value indicating that it was not found.

Example run:
```
 L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
 L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]
```

Psuedocode:
```
// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
```

Stub:
```python
def binary_search(nums, value):
  ...
#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
```



## Part 3 - Bubble Sort

[Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

```
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped = false
        for i := 1 to n - 1 inclusive do
            /* if this pair is out of order */
            if A[i - 1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure
```

## Part 4 - Insertion Sort (optional)

Implement [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), which like bubble sort is also `O(n^2)`, but is efficient at placing new values into an already-sorted list.

Psuedocode:
```
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
```


## Part 5 - Quicksort (optional)

[Quicksort](https://en.wikipedia.org/wiki/Quicksort) is one of the most efficient sorting algorithms. It works by swapping elements on either side of a pivot value.

Psuedocode:
```
algorithm quicksort(A) is
    quicksort_recursive(A, 0, length(A) - 1)

algorithm quicksort_recursive(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort_recursive(A, lo, p)
        quicksort_recursive(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[lo + (hi - lo) / 2]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot
        do
            j := j - 1
        while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]
```


