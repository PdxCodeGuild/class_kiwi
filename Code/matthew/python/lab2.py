'''
Lab 2
Average numbers
'''
# --- Version 1
'''

nums = [1,2,3,4]
running_count = 0

for num in nums:
    
    running_count += num  
    
average = running_count / len(nums)

print(average)

'''

# --- Version 2

nums = []
running_count = 0

while True:
    nums += input('Enter a number or press "q" to quit ')
    if nums[-1] == 'q': 
        break

nums.pop(-1)

for num in nums:
    running_count += int(num)

average = running_count / len(nums)
print(f'The average of the numbers you entered is {average}')





          











