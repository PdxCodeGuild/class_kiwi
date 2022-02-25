"""
Peaks And Valleys
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/18/2022
"""


test_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def is_peak(counter,data):
    # if the numbers before and after in the data are smaller 
    # than the current digit then return true

    if counter == 0 :
        return False
    elif counter + 1 >= len(data):
        return False
    number_before = data[counter - 1]
    number_after = data[counter + 1 ]
    current_digit = data[counter]
    
    

    print(number_after)
    print(number_before)
    print(current_digit)

def peaks(data):
    peaky = []
    for counter, num in enumerate(data):
        if is_peak(counter,data):
            peaky.append(counter)
    return peaky
cat = peaks(test_data)
print(cat)