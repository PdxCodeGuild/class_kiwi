# average a list of numbers
#keep a running sum
#divide / the sum by the number of elements
#len
#add all the numbers up than divide by how many numbers there are
#for each element in _____do the following
# num = int(5 + 0 + 8 + 3 + 4 + 1 + 6)
# print(f'{num}')

# print(f"the avarage {num/ 7} ")

num = [5,0,8,3,4,1,6]
total = 0
for numbers in num:
    print(numbers)
    total = numbers + total 
print(total)   
a = len(num) 
print(a)

print(f'the average {round(total/a)}')
