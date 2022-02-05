# Lab 2 Version 2

# empty list

nums = []
sum = 0
while True:
    number = input("enter a number, or 'done':")
    if number == "done":
        break
    number = int(number)
    nums.append(number)
    sum = number + sum

average = sum/len(nums)
print(f"average: {average}")
