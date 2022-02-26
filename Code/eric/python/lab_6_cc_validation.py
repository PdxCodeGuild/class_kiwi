##Lab 6 Credit Card validation

#Take a number and verify it is a valid credit card number

#convert input string into a list

number = input('Enter your credit card number: ')

#create a for loop to build the list
number_broken = []

for i in number:
    number_broken.append(int(i))

#slice off the last digit
last_digit = number_broken.pop(-1)

#reverse the digits
number_broken.reverse()

#double every other element
for i in range(0, len(number_broken), 2):
    number_broken[i] *= 2 
    
# from class
# for index, value in enumerate(number):
    # if index % 2 ==0:
    #     number[index] = number_broken * 2

#subtract 9 from numbers over 9
for i in range(0, len(number_broken)):
    if number_broken[i] > 9:
        number_broken[i] -=9
    
#sum all values
summed_up = sum(number_broken)

#take the second digit of sum
second_digit = summed_up % 10

#compare the second digit to the pooped digit

if second_digit == last_digit:
    print(f'{number} is a valid credit card number')
    
else:
    print(f'{number} is not valid')
    
    
