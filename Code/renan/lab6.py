#Credit Card Validator
#4556737586899855
# card_number = input("What is the card number?: ")

# c_card =[]
# for char in c_card:
#         c_card.append(int(char))

#Another Option (python is reading this from right to left..for every number in this list..convert to int)
#nums = [int(char) for char in card_number]
card_number = '4556737586899855'




#Convert input strings to list
def credit_card_validator():
    nums = list(card_number)

    for i in range(len(nums)):
        nums[i] = int(nums[i])
        print(int(nums[i]))

    print(nums)

    #Slice off the last digit (now called check digit)
    check_digit = nums.pop()

    #Reverse List
    nums = nums[::-1] 
    print(nums)

    #Another method to reverse the list
    # check_digit.reverse()
    # nums = list(reversed(nums)

    #Double every other element in the reversed list
    for x in range(0, len(nums), 2):
        nums[x] += nums[x]

    print(nums)

    #Option 1
    # for index, value in enumerate(nums):
    #     if index % 2 == 0:
    #         nums[index] = value *2

    # Subtract nine from numbers over nine.
    #Option 1
    for index, value in enumerate(nums):
        if value > 9:
            nums[index] = value - 9

    print(nums)

    # Sum all values.
    total = sum(nums)

    print(total)


    # Take the second digit of that sum.

    last_digit = total % 10

    print(last_digit)

    # If that matches the check digit, the whole card number is valid.
    if last_digit == check_digit:
        return True
    else:
        return False
    
print(credit_card_validator())