# Lab 2: Average Numbers

# # Number List
nums = [5, 0, 8, 3, 4, 1, 6]

sum = 0
# # run through list and keeping a running sum
for num in nums:
    sum = num + sum
    print(sum)

# # divide sum by number of elements in that list
sum = sum/len(nums)
print(round(sum, 2))
