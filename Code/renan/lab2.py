#Version 1 Print Elements and Average Numbers
nums = [5, 0, 8, 3, 4, 1, 6]
average = sum(nums) / len(nums)

for i in range(len(nums)):
    print(nums[i])
    

for num in nums:
    print(average)
        


   
  
#Version 2 user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average
numss = [] 

while True: 
    user_choice = input("Enter a number or done: ") 
    if user_choice == "done":
        break
    numss.append(float(user_choice))

for n in numss:
    print(n)   

average = sum(numss) / len(numss)

for n in numss:
    print(average)
      


