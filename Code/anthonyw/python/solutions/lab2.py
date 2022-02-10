# We're going to average a list of numbers. 
# Start with the following list, iterate through it, keeping a 'running sum', 
# then divide that sum by the number of elements in that list. 
# Remember len will give you the length of a list.

def average_of_nums(nums):
    total = 0
    # iterate over numbers
    for num in nums:
        # keep track of running total
        total += num

    # get average of all numbers
    average = total / len(nums)

    return average

# use sum function instead of iterating over list
# average = sum(nums) / len(nums)

def main():
    # Output result
    nums = [5, 0, 8, 3, 4, 1, 6]

    average = average_of_nums(nums)

    print(f"The average of all numbers is {average:.2f}")

# If imported __name__ would == 'lab2'
if __name__ == '__main__':
    main()