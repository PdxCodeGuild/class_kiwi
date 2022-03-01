#Version 1 
#add the numbers together from a list and devide them by length

# nums = [5, 0, 8, 3, 4, 1, 6]

#printing out the list of numbers
# print("These are your numbers:")
# for num in nums:
#     print(num)

#the easy way?

# #summing numbers together
# sums=sum(nums)
# print(f"They add up to {sums}")

# #creating the pipe to make the average
# div=len(nums)
# average=sums/div
# print(f"The average is {div}")

#the loop way

# print("These are your numbers:")
# for num in nums:
#     print(num)

# for i in range(len(nums)):
#     nums[i] = nums[i] + nums[0]
#     print(nums)

# total = 0
# for i in nums:
#     total = total + i
#     print(total)

#version 2

# create the empty matrix
nums=[]

#create a loop for user input into the list

while True:
    print("Enter a number or type done when finished: ")

    numbers = input()
    
    if numbers == 'done':
        break

    else:
        nums.append(numbers)
        
print(f'These are your numbers: {nums}')  

#converted each to an integer
for i in range(len(nums)):
    nums[i] = int(nums[i])
  
sums=sum(nums)

#divide out the length for the average

div=len(nums)
average=sums/div

print(f'The average is: {average}')