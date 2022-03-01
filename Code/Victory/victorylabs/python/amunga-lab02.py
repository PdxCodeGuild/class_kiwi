'''Version 1'''
#Using for loops, create a function that produces an output that is the average of the list
nums = [5, 0, 8, 3, 4, 1, 6]

def sum_of_list(n):


    nums = 0

    for num in n:
        nums += num
    
    return nums



print(sum_of_list(nums))

def len_of_list(m):

    numbers = 0

    for num in m:
        numbers += 1
    return numbers

print(len_of_list(nums))

aver_age = sum_of_list(nums)/len_of_list(nums)

print(round(aver_age,1))


'''Version 2'''

#Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average.



print('\nProvide some numbers to create a list and I will add them ')

users_list = []

while True:

    user = input('Please enter a number: ')

    if user == 'done':
        break

    else:
        users_list.append(int(user))

#print(users_list)

average_of_userlist = sum_of_list(users_list) / len_of_list(users_list)

print(f"Elements in your list are {users_list}, the sum of that list is {sum_of_list(users_list)}, list length is {len_of_list(users_list)}, average of the list is {average_of_userlist}  ")
