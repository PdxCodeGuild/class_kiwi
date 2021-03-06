# Lab 2: Version 2
# List items and length of list determined by user
nums_list = []

# Loop will continue until 'done' breaks loop
while True:
    nums = input("Enter a number or 'done': ")
    
    if nums.lower() == 'done':
        break

# Would like to exclude invalid entries, including spelled numbers.
    elif nums.isnumeric() == False:   # Referenced W3Schools -pyton string methods for 'isnumeric' method
        print("Please enter a valid number or 'done'")
        continue

    else:
        nums = int(nums)      # string changed to int
        nums_list.append(nums)

# Display entered numbers
print(f'You entered the following numbers: {nums_list}')

# All nums looped, added together and assigned to num_sum
num_sum = 0

for num in nums_list:
    num_sum += num

# function to average the sum of all numbers in the list by the length of list
def average(num_sum):
    num_average = num_sum/len(nums_list)
    return num_average

# Final message
print(f'The average is {round(average(num_sum), 4)}')
    