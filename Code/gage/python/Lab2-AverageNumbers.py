

'''

VERSION 1


nums = [5, 0, 8, 3, 4, 1, 6]
# Running sum is a place holder for the total sum to be placed into
running_sum = 0

# This list adds every number in the list together and stores it into the running sum
for numbers in nums:
   running_sum += numbers

# Divides the total sum by the length of the list
print( f"The average number is {running_sum / len(nums)}")

'''


'''
VERSION 2

# Place holder list for the users numbers to appened to
nums = []
# Base value to check wether or not to end the loop
again = True

while again == True:

    user_num = input("Enter a number or type 'done' to exit: ")

# If the user enters a number it will convert the string into a float and append it the the base list
    if user_num != 'done':
        nums.append(float(user_num))
# If the user types 'done' the loop will end
    else:
        again = False

running_sum = 0

for numbers in nums:
   running_sum += numbers

print( f"The average number is {running_sum / len(nums)}")

'''