# Version 1
# Original list of numbers
numbers = [5, 0, 8, 3, 4, 1, 6]

# iterating through list and adding sum
for num in range(len(numbers)):
    print(numbers[num])
    num += num

# creating variable to find average of list and printing results
num_sum = sum(numbers) // len(numbers)
print(f"Average: {num_sum}")
   
"""    
#Version 2
new_list = []
# collecting user input for numbers in list
while True:
    user_input = input("Please enter in a number or type 'done' to exit: ") 
    if user_input == "done":
        break
    new_list.append(int(user_input))

# adding new list items together
total = 0
for item in new_list:
    total += item

# printing average of new number list 
average = total / len(new_list) 
print(average)
"""