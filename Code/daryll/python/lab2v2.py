nums = []
while True:
    input_numbers = input("Enter a number, or 'done': ")
    if input_numbers == 'done':
        break
    else:
        nums.append(input_numbers)
counter = 0
for num in nums:
    counter += int(num)
print(f"average: {counter / len(nums)}")