import random

import lab2


def generate_numbers():
    numbers = []
    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)

    return numbers

# def test_average_of_nums():
#     # nums1 = generate_numbers()
#     # nums2 = generate_numbers()

#     # assert lab2.average_of_nums(nums1) == sum(nums1) / len(nums1)
#     # assert lab2.average_of_nums(nums2) == sum(nums2) / len(nums2)

#     for i in range(12):
#         numbers = generate_numbers()
#         if i == 3:
#             assert lab2.average_of_nums(numbers) == sum(numbers) / 1
        
def test_average_of_nums_valid():
    numbers = generate_numbers()
    assert lab2.average_of_nums(numbers) == sum(numbers) / len(numbers)

def test_average_of_nums_invalid():
    numbers = generate_numbers()
    numbers.append('llama')
    assert lab2.average_of_nums(numbers) == 'Invalid operation'

def test_average_of_nums_len_0():
    numbers = []
    assert lab2.average_of_nums(numbers) == False