import lab02


def main():
    nums = []
    while True:
        entry = input("Enter a number or 'done': ")
        if entry == 'done':
            break
        else:
            nums.append(float(entry))

    average = lab02.average_of_nums(nums)
    print(f"The average of numbers is: {average}")
        


if __name__ == '__main__':
    main()