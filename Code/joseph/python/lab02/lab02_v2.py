#Lab 02 - Average Numbers - Version 2 - Working

#define empty list nums
nums = []

#start a while loop asking for user input, breaking if done is entered, asking user to 
#re-enter the number if a non-integer is input, appending list nums with the integer of the user input
while True:
    num = input('Please enter at least one integer to continue or "done" to end: ')
    if num == 'done':
        break
    try:
        nums.append(int(num))
    except ValueError:
        print('That is not an integer, please try again')
    
#Maths
average = sum(nums) / len(nums)

#Print output
print('The Average is ' + str(round(average, 2)))