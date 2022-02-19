# Average numbers

# nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])


nums = []
while True:
    user = input("Enter numbers one at a time, or 'done'. ")
    
    
    if user == "done":
        break
    else:
        user = int(user) 
        nums.append(user) 
        continue
total = 0
for num in range(len(nums)):
    
    total += nums[num]
    print(total)
answer = total / len(nums)   
print(answer)






