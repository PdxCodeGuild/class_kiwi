# Lab 2: Average Numbers

# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember `len` will give you the length of a list.

# The code below shows how to loop through an array, and prints the elements one at a time.
# loop over the indices



nums = [5, 0, 8, 3, 4, 1, 6]

#set a new variable = 0; to initialize iterative summation 
def average_of_nums(nums):
    sum_total = 0
    for i in range(len(nums)):
        sum_total += nums[i]
        avg = sum_total/len(nums)
# #Get the length of the list 

# #Average the total numbers added by the list length 

# avg = round((avg),2)
# #print(avg)

## Version 2

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. 
user_num_list = []

while True:
    user_num_entry = (input ('Enter a list of numbers one at a time, or type "done" if finished: '))
    user_num_list.append(user_num_entry)
    if user_num_entry == 'done':
        break
    elif user_num_entry != 'done':
        user_num = int(user_num_entry)
        user_num_list.append(user_num)

print(user_num_list)
# for i in range(len(user_num_list)):
#     user_num += user_num_list
#     total_items = len(user_num_list)

# avg = user_num/total_items
# avg = round((avg),2)


# print (avg)


# 
#     if user_num_entry >= 0: 
#         while True:
#             user_num_entry = (input('Enter a list of numbers one at a time, or type "done" if finished: '))
#             if user_num_entry == 'done':
#                 print(f'Your average is: {(user_num_entry/total_items)}.')
        

#     user_num_entry = input("\nEnter a list of numbers one at a time: ")
#     user_num_entry = int(user_num_entry)
#     user_num_entry = nums.append(user_num_entry)
#     if user_num_entry == 'done':
  
#          break 
