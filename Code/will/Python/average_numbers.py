# Version 1 - Number Average

#def average(numbers):
#    total = 0
#    for num in numbers:
#        total += num
#    average = total / len(numbers)
#    return average

#def main():

#    numbers = [5, 0, 8, 3, 4, 1, 6]

#    average_of_list = average(numbers)

#    print(f"The average of the number list provided is {average_of_list:.2f}.")

#main()


# Version 2 - Number Average

def average(numbers):                                                                                   # function for getting the average of the input list
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average


def main():

    numbers = []                                                                                        # empty list
    
    while True:                                                                                         # while loop to allow user to add as many numbers as they desire

        user_input = input("Enter a number to add to the list, or 'done' to average your list: ")
        user_input = user_input.lower()

        if user_input == 'done':                                                                        # loop exit
            print('Calculating....')
            break

        else:                                                                                           # try/except to catch inputs that aren't numbers
            try:
                user_input = int(user_input)
            
            except ValueError:
                print('Only numbers are valid entries.')

            else:
                numbers.append(user_input)


    average_of_list = average(numbers)                                                                  # feed completed list to function and display result
    print(f"The average of the number list provided is {average_of_list:.2f}.")

main()