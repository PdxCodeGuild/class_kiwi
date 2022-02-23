# version 1

nums = [5, 0, 8, 3, 4, 1, 6]

holder = 0

for num in nums:
    holder += num

answer = holder/ len(nums)

print(round(answer, 2))


#version 2


print("")

num_list = []
loop = True

while loop:
    question = input("enter a number or type done: ")

    if question != "done":
        num_list.append(int(question))

    else:
        loop = False

sum = 0

for number in num_list:
    sum += number
    

answer = sum / len(num_list)
print(f"The avarage of your numbers is {answer}")
