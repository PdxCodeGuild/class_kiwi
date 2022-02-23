import random

#import amunga_lab02

def gen_nums():

    numbers = []

    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)
    
    print(numbers)

print(gen_nums())

def test_average_of_nums():

    num1= gen_nums()
    #num1 = gen_nums()

    aver_age = sum(num1) / len(num1)

#print(test_average_of_nums(gen_nums))

len_of_list = len(gen_nums())
print(len_of_list)

