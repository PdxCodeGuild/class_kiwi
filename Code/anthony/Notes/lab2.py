###  Lab 2 Practice  ###
################################
##                            ##
## Lab 2: Average Numbers     ##
##   Author: Anthony Bilie    ##
##   Date: 2/13/2022          ##
##                            ##
################################

# We're going to average a list of numbers.
# Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list.
# Remember len will give you the length of a list.
# The code below shows how to loop through an array, and prints the elements one at a time.

# list of numbers
nums = [5, 0, 8, 3, 4, 1, 6]

# iterate through list and keep a running sum
sum = 0
for x in nums:
    sum += x
print(sum)


# divide sum by number of elements in the list.
average = (sum/len(nums))
print(round(average, 2))
