###  Lab 2 Practice  ###
################################
##                            ##
## Lab 2: Average Numbers     ##
##   Author: Anthony Bilie    ##
##   Date: 2/16/2022          ##
##                            ##
################################
# Version2

# Ask the user to enter the numbers one at a time, putting them into a list.
# If the user enters 'done', then calculate and display the average.
# The following code demonstrates how to add an element to the end of a list.
import lab2
# empty ist
nums = []
# ask user to input numbers on at a time and append to empty list
# use while loop and stop if user enters done
while True:
    answer = input("Please enter a number or enter done to quit: ")
    if answer == "done":
        break
    else:
        answer = int(answer)
        nums.append(answer)
# calculate and display average
total = lab2.total(nums)
# calculate and display average
average = total/len(nums)
# output
print(f"The average is {average}.")
