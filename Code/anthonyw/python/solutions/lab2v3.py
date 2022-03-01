import lab2

# while True:
#     entry = input("Enter a number: ")

#     try:
#         number = int(entry)
#         break
#     except ValueError:
#         print(f"Invalid entry. {entry} is not a number.")

# print('Hooray, I finished the program without errors.')


def main():

    nums = []
    # repeatedly ask user for numbers
    while True:
        entry = input("Enter a number or 'done': ")
        if entry == 'done':
            break
        else:
            try:
                nums.append(float(entry))
            except ValueError:
                print(f'Invalid input, {entry} is not a number')
    
    average = lab2.average_of_nums(nums)
    print(f"The average of numbers is: {average:.2f}")


if __name__ == '__main__':
    main()