# Lab 2

# *** Version 1 ***

nums = [5, 0, 8, 3, 4, 1, 6] 

# create counter
num_sum = 0

#loop through nums list and print average
for num in nums:
    num_sum += num
    print("running sum: ", num_sum)
print("average: ", (num_sum/len(nums)))


# *** Version 2 ***

'''

# create empty list
nums = []

# get user inputs
while True:
  input_number = input("Enter a number, or 'done': ")

  if input_number == 'done':
    break 

  # convert input to integer
  input_number = int(input_number)

  # append to list
  nums.append(input_number)

# add numbers in list
nums_sum = sum(nums)

# get the number of items in list
nums_count = len(nums)

# get average
nums_avg = nums_sum/nums_count

# print results
print("average:", nums_avg)
'''














