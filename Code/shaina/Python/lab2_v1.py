# Lab 2: Version 1

# Identify list
nums = [5, 0, 8 , 3, 4, 1, 6]

# All numbers added together and assigned to num_sum
num_sum = 0

for num in nums:
    num_sum += num

# function to average the sum of all numbers in the list by the length of list
def average(num_sum):
    num_average = num_sum/len(nums)
    return num_average

print(average(num_sum))    