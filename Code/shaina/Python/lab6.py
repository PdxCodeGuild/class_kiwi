# Lab 6: Credit Card Validation
"""
Let's write a function `credit_card_validator` which returns whether a string containing a 
credit card number is valid as a boolean. The steps are as follows:
1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list (starting with the first number in the list).
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.

Here is a valid credit card number to test with: 4556737586899855
For example, the worked out steps would be:
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. `True` Valid!
"""

card_num = list(input("Please enter a credit card number: "))
print(card_num)  # step 1

check_digit = int(card_num[-1])  # step 7

card_num = card_num[slice(0, 15)]
print(card_num)  # step 2

card_num.reverse()
print(card_num)  # step 3

index = 0
for i in card_num[::2]:
    i = (int(i) * 2)
    card_num.pop(index) 
    card_num.insert(index, i)
    index += 2
print(card_num) # step 4

def sum(card_num):    # step 5 and 6
    sum = 0
    for i in card_num:
        if int(i) > 9:
            num = int(i) - 9
            sum += num
        else:
            num = int(i)
            sum += num    
    return sum
print(sum(card_num))

def verify():
    verify = sum(card_num)%10
    return verify
print(verify())
print(check_digit)  # step 8

if verify() == check_digit:
    print(True, 'valid')

else:
    print(False, 'invalid')