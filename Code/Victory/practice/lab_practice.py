'''
#Enumerate prints the index and the list at same time.
letts = ['a', 'b', 'c', 'd']

for i, let in enumerate(letts):
    print(i, let)

for let in(letts):
    print(let)

for i in range(len(letts)):
    print(i)
#Equivalent of enumerate for dictionaries
grades = {
    1:1, 2:2, 3:3
}
for key, value in grades.items():
    print(key, value)

'''

card_number = list(input('Please enter the card number: '))
check_digit = card_number.pop()

card_number.reverse()

sum_numbers = []

for index, i in enumerate(card_number):

    if index % 2 ==0:
        sum_evenindex = int(i) * 2
        if sum_evenindex > 9:
            sum_evenindex = sum_evenindex - 9

        sum_numbers.append(sum_evenindex)
    else:
        sum_numbers.append(int(i))

total = sum(sum_numbers)
print(total)

if total[-1] == check_digit:
    print('Valid Card!')

else:
    print('Invalid Card')

