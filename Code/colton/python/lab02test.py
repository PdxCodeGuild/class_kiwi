'''         +-+#^#+--+#^#+--+#^#+-+             
            Project: Average Numbers              ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/3/22                     ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''
# Version 1

import time

def average(numbers):
    """This will get sum of a list and divide the sum by the length of the list getting the average"""
    x = 0
    a = 0
    for number in numbers: # for each number in a list
        a += number # add the sum of each number to a
        x = a / len(numbers) # take the sum of a and divide it by the total iterations in list
        x = round(x, 2) # round the result by two decimal points
    return x


nums = [5, 0, 8, 3, 4, 1, 6]

print(average(nums))
time.sleep(2)

# Version 2

# Get user input and give an average 

nums = []

while True:
        user_input = float(input("Enter a number or 'done' to end equation:  ")) # repeats question until user wants result
        if user_input =="done":
            print(f"You entered: {nums}")
            print(f"Your average is {average(nums)}")
            time.sleep(3)
            break
        elif user_input ==ValueError:
            print("erererer")
        elif user_input ==float:
            nums.append(user_input) # converts user input to an int and adds it to nums list
            continue
       
        

        else:
            print("Enter valid input")
        
time.sleep(5)

