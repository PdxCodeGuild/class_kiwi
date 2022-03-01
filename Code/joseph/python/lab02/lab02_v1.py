# Lab 02 - Average Numbers - Version 1 - Working

# define the list
nums = [5, 0, 8, 3, 4, 1, 6]

#create empty list to store running sum
rsum = []

#Define starting at 0
r = 0

#iterate through list nums, adding each element to r then appending list rsum with r, printing the running sum after each element
for num in nums:
    r += num
    rsum.append(r)
    print(rsum[-1])

#maths
average = sum(nums) / len(nums)

#print output
print('The Average is ' + str(round(average, 2)))