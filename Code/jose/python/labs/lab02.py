

#  First write the code for what is shown in the example run it through and understan what is going on
#  next get the sum of these numbers

# nums = [5,0,8,3,4,1,6]
###############################################
# loop over the elements
# for num in nums:
#     print(num)  

# #############################################
# # loop over the indeices
# for i in range(len(nums)):
#     print(nums[i])

# nums = [5,0,8,3,4,1,6]
# print(type(nums[0]))


# #  VERSION 1
# nums = [5,0,8,3,4,1,6]
# total = 0
# for num in nums:
#     total += num 
#     sum = (total / len(nums))
#     sum = round(sum, 2)
# print(sum)
    

# VERSION 2
# Asking user to enter numbers and type done to run and get the average
#  I will start by copying my last code to set a foundation and work my to add remove and enter what i need

# Create a list to allow something to be added


# print("The some of your numbers are ___")
# nums = []

# while True:
#     user_nums = (input("enter a number, or 'done'"))
#     nums.append(user_nums)
#     if user_nums == 'done':
#         break
    
# total = 0
# for num in nums:
#     total = int(num) + total
#     sum = (total )
#     sum1 = round(sum, 2)

# print(sum1)

###############################################################################

nums = [5,0,8,3,4,1,6]

def average_of_nums(nums):
    total = 0

    for num in nums:
        total += num

    average = total /len(nums)
    return average


def main():

    nums = [5,0,8,3,4,1,6]

    average = average_of_nums(nums)

    print(f"The average of all numbers is {average:.2f}")

# if imported __name__ would == 'lab2'
if __name__ == '__main__':
    main()
