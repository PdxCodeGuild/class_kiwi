# average a list of numbers
#keep a running sum
#divide / the sum by the number of elements
#len
#add all the numbers up than divide by how many numbers there are
#for each element in _____do the following
# num = int(5 + 0 + 8 + 3 + 4 + 1 + 6)
# print(f'{num}')

# print(f"the avarage {num/ 7} ")

########################################################

# Version 1
# def average_list(num):
#     total=0
#     for number in num:
#         total = total + number 
#     return(total/len(num))

# a = [1,2,3]
# print(average_list(a))

########################################################
# num = [5,0,8,3,4,1,6]
# total = 0
# for numbers in num:
#     print(numbers)
#     total = numbers + total 
#     #Provides me with the list of numbers and also adding each number together
# print(total)  
# a = len(num) 
#     #len provides me with the count of each character in the list
# print(a)

# print(f'the average {round(total/a)}')
#     # the round function allows me to the closes digit. I divided the total by the number of _ in the list.



########################################################


# Version 2
# total = 0
number_list = []
while True:

    numm=input(f'give me a number and or enter done: ' )
    if numm == "done":
        break
    elif numm != "done":
        # int(numm)
        number_list.append(int(numm)) 
        

print(number_list)

print(average_list(number_list))


#find average of list of numbers(add all the numbers divide by how many numbers there are.)

########################################################
# nums = [5, 0, 8, 3, 4, 1, 6]
# total = 0
# for num in nums:
#     total = num + total
# print(total)
    

########################################################
 
 #find the average of the list of numbers(average is the total numbers / by the amout)
 #
 
 
 
# nums = [5, 0, 8, 3, 4, 1, 6]
# total = 0
# for num in nums:
#     total = num + total
# print(total)

# print(total_numbers)
# total_numbers

########################################################
# numbers = [5,2,3,2,6,7,8]
# total = 0
# for each_element in numbers:
#     total = each_element + total
# print(total)
# number_items_in_a_list = len(numbers)
# print(number_items_in_a_list)
# average = (total / number_items_in_a_list)

# print(F'the average is: {round(average)}')

########################################################

# list_of_numbers = [4,2,5,7,1,9,9]
# a = 0
# for total in list_of_numbers:
#     a = a + total
# print(a)
# average = a / len(list_of_numbers)
# print(f'{round(average)}')  

########################################################

# list = [2, 2, 4, 5, 6, 7, 8]
# count = 0
# for total in list:
#     print(total)
#     count = total + count
# print(count)
# average = count / len(list)
# print(f'{round(average)}')
########################################################

# list = [8, 5, 9, 8, 9, 1, 7, 8]
# total = 0
# for a in list:
#     print(a)
#     total = total + a
# print(total)
# average = total / len(list)
# print(average) 
# print(f' {round(average)}')

########################################################

# fruits = ["appel", " bannan", "citrus"]

# fruits.append("dragon fruits")

# print(fruits)


# list = [4, 6, 7, 8, 9, 9, 9]
# a = 0
# for b in list:
#     a = b + a
# print(a)
# c = len(list)
# print(a / c)

# list = [3, 9, 8, 7, 9, 9, 8]
# total = 0
# for all_num in list:
#     print(all_num)
#     total = all_num + total
# print(total)
# average = total / len(list)
# print(average)
# print(f'{round(average)}')







# average a list of numbers
#keep a running sum
#divide / the sum by the number of elements
#len
#add all the numbers up than divide by how many numbers there are
#for each element in _____do the following
# num = int(5 + 0 + 8 + 3 + 4 + 1 + 6)
# print(f'{num}')



# def average_of_nums(nums):
#     total = 0
# # iterate over numbers

# for num in nums:
#     # keep track of running total
#     total += num

# # get average of all numbers
#     average = total/ len(nums)

# def main():
# #output result
#     nums = [5, 0, 8, 3, 4, 1, 6]

#     print(f' The average of all numbers is {average:.2f}')



