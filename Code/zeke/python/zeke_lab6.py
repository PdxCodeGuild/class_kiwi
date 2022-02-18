
# 1Convert the input string into a list of ints
# 2Slice off the last digit. That is the check digit.
# 3Reverse the digits.
# 4Double every other element in the reversed list (starting with the first number in the list).
# 5Subtract nine from numbers over nine.
# X6Sum all values.
# 7Take the second digit of that sum.
# 8If that matches the check digit, the whole card number is valid.
# 9Here is a valid credit card number to test with: 4556737586899855

# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# True Valid!

#a function credit_card_validator which returns 
#  a string containing a credit card number 
# is valid as a boolean.

def credit_card_validator():
    #     card number is the variable name contianing our string
    card_number = []
    #    number_string is the user input of a string of numbers
    numbers_string = input(f'please enter a valid card number: ')
    #    creating a NEW VARIABLE for EACH number identified number to begin looping.
    #    number will loop each .appended number into intergers.
    for number in numbers_string:
        card_number.append(int(number))
    
    #creating a new variable, check_digit to run .pop/ .POP is a METHOD that allows 
    #   us to store and pop off the last digit into a variable that we can reuse later if need be.
    check_digit = card_number.pop()
    #   now that we have our list of numbers known as card 
    #   number, we will use the .reverse METHOD to reverse the order of the numbers.
    card_number.reverse()

    #   Createing a new varable counter, counter will allow us to keep track of the second digit 
    #   that we will use to double every other digit.
    counter = 0
    #   card_number has now turned into a method that we can store into another variable such as num.
    #   for each  num the if statement below will run.
        
    for num in card_number:
    #    ----------NEED HELP UNDERSTING THIS PART.---------------

    #   Modulo % doubles each number when by 2. example 4%2 = 0.8
        if counter % 2 == 0:
    #   the METHOD "pass" stops the modulo from continuing
     
            num = num * 2
    #   for each position counter?????
            card_number[counter] = num
        counter = counter +1
    
    counter = 0
    for num in card_number:
        if num >9:
            num -= 9
            card_number[counter] = num
        counter = counter +1

    list_sum = sum(card_number)
    print(list_sum)
    last_digit = list_sum % 10
    print(last_digit)
    if last_digit == check_digit:
        # print('Valid credit card')
        return True
    else:
        # print('Invalid card number')
        return False
    #     card_number.append(numbers_list)
    # print(card_number)

print(credit_card_validator())




    # check_digit = card_number[-1]
    # card_number

valid_number= 4556737586899855