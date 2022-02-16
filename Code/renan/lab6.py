#Credit Card Validator

card_number = input("What is the card number?: ")
#Convert input strings to list
nums = list(card_number)

for i in range(len(nums)):
    nums[i] = int(nums[i])
    print(int(nums[i]))

#Slice off the last digit (now called check digit)
check_digit = nums [0:15]

print(check_digit) 

#Reverse List
check_digit.reverse()

print(check_digit)


