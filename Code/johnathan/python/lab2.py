
# # Lab 2: Average Numbers

# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember `len` will give you the length of a list.

# The code below shows how to loop through an array, and prints the elements one at a time.


# loop over the indices
nums = [5, 0, 8, 3, 4, 1, 6]

#set a new variable = 0; to initialize iterative summation 
sum_total = 0
for i in range(len(nums)):
   sum_total += nums[i]
#Get the length of the list 
total_items = len(nums)
#Average the total numbers added by the list length 
avg = sum_total/total_items

print(round(avg,2))

# ```

# ## Version 2

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

# ```python
# nums = []
# nums.append(5)
# print(nums)
# ```

# Below is an example input/output:


# ```
# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4
# ```