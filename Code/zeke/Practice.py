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

# #creating a funcation to reuse 
#     total=0
#     for number in num:
#         total = total + number 
# #     #The list of numbers adding each number together
#     return(total/len(num))
# #     #len provides me with the count of each character in the list of ( ) in which i divide by the total 
# a = [1,2,3]
# print(average_list(a))


# # num = [5,0,8,3,4,1,6]
# def x():
#     num = [5,0,8,3,4,1,6]
#     total = 0
#     for numbers in num:
# print(numbers)
#     # total = numbers + total 
#     # print(total)  
#     # a = len(num) 

#     # print(a)

# # print(f'the average {round(total/a)}')
# #     # the round function allows me to the closes digit. I divided the total by the number of _ in the list.



# ########################################################


# # Version 2

# number_list = []
# total = 0
# while True:

#     numm=input(f'Enter a number or enter done:  ')
#     if numm == "done":
#         break
#     elif numm != "done":
#         number_list.append(numm)
#     elif total == total + number_list/len(numm):

# print(number_list)  




# # number_list = []
# while True:

#     numm=input(f'give me a number and or enter done: ' )
#     if numm == "done":
#         break
#     elif numm != "done":
#         number_list.append(numm) 

# print(number_list)


########################################################

dictionaries
pet = {"name":"Rocky", "breed": "rock", "size": "large", "nickname": "roxie"}

print(pet["name"])


# .get#The get() method returns the value of the item with the specified key.
# .update#.update updates a key:value in a dictionary
#.keys#method to get all keys from dictionary
#.values#method to get all values
value = pet.value()
#.items#method to get all Key:value from dictionary
pairs = pet.items()



if num <100:
    tens_digits = num //10#8
    ones_digits = num%10#4
    
#     # test_word = numbers[tens_digits] + " - " + numbers[ones_digits] # ones_digit[8],numbers [4]
    
    if num <10:
        print(ones_digits)
        print(numbers[ones_digits])

    elif num >10 and num <= 19:
        print(f'{numbers[num]}')
   
    elif num >=10:
        tens_digits = tens_digits * 10 

        print(tens_digits)
        print(f'{msc[tens_digits]}{numbers[ones_digits]}')

    elif num <20:
        print(f'{numbers[tens_digits]}{numbers[ones_digits]}')
