import lab2

# Ask the user to enter the numbers one at a time, 
# putting them into a list. If the user enters 'done', 
# then calculate and display the average.
# [5, 0, 8, 3, 4, 1, 6]

def main():

    nums = []
    # repeatedly ask user for numbers
    while True:
        entry = input("Enter a number or 'done': ")
        if entry == 'done':
            break
        else:
            nums.append(float(entry))
    
    average = lab2.average_of_nums(nums)
    print(f"The average of numbers is: {average:.2f}")


if __name__ == '__main__':
    main()