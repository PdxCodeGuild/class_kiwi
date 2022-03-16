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
    if current_digit > number_after and current_digit > number_before:
        return True

def is_valley(counter,data):
    
    if counter == 0:
        return False
    elif counter + 1>=len(data):
        return False
    number_before = data[counter - 1]
    number_after = data[counter + 1 ]
    current_digit = data[counter]
    if current_digit < number_after and current_digit < number_before:
        return True
def valleys(data):
    vallee = []
    for counter, num in enumerate(data):
        if is_valley(counter,data):
            vallee.append(counter)
    return vallee
def peaks_and_valleys(data):
    p_and_v = []
    for counter, num in enumerate(data):
        if is_valley(counter,data):
            p_and_v.append(counter)
        if is_peak(counter,data):
            p_and_v.append(counter)
        
    # for x in peaks:
    #     p_and_v.append(x)
    # for x in valleys:
    #     p_and_v.append(x)
    
    return p_and_v
    

    # print(number_after)
    # print(number_before)
    # print(current_digit)

def peaks(data):
    peaky = []
    for counter, num in enumerate(data):
        if is_peak(counter,data):
            peaky.append(counter)
    return peaky
cat = peaks(test_data)
print(cat)
mouse = valleys(test_data)
print(mouse)
pup = peaks_and_valleys(test_data)
print(pup)