'''
Lab 2
Average numbers
'''
# --- Version 1
'''

nums = [1,2,3,4]
running_count = 0  # will add num to running count

for num in nums:
    
    running_count += num  # adding num to running count
    
average = running_count / len(nums)  # averaging running count using len of nums

print(average)

'''

# --- Version 2

# same as version one with the acception that nums is an empty list and is filled by user input


nums = []
running_count = 0 

while True:
    nums += input('Enter a number or press "q" to quit ')  # filling nums list
    if nums[-1] == 'q': 
        break

nums.pop(-1)

for num in nums:  # cycling over each indavidual indcie (idk how to spell it) and adding it to running_total
    running_count += int(num)     

average = running_count / len(nums)  # same as before averaging running count using len of numbers
print(f'The average of the numbers you entered is {average}')  # 





          











