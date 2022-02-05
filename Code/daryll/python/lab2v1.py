nums = [5, 0, 8, 3, 4, 1, 6]
counter = 0
for num in nums:
    counter += int(num)
print(f"average: {counter / len(nums)}")