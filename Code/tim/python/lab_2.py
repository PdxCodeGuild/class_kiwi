"""
Average Numbers
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/4/2022
"""

# I want to avg a list of numbers
#  we will go through the list keeping a running sum
# Then divide that sum by the number of elements in that list. 
# **Tip len will give you a length of list



# nums = [5, 0, 8, 3, 4, 1, 6]




def average_calc(nums):
    for x in nums:
        digit_amt = len(nums)
    total = sum(nums)

    avg = total / digit_amt
    
    print(avg)
    return avg



# average_calc(nums)

########## Version 2 ###########

# Here we seek to ask for an input of numbers 1 at a time. 

numberlist = []
user_pick = input("Please enter a number or 'done' " )
while user_pick != "done":
    user_pick = input("Please enter a number or 'done' " )
    if user_pick == "done":
        break
    user_pick = int(user_pick) 
    numberlist.append(user_pick)
    
average_calc(numberlist)




