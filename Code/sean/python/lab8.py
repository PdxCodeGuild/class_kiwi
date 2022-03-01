
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    data_len = len(data) - 1   #getting length of list -1

    for i in range(0, data_len):        #starting at index 0 then looping through length of data list
        
        if data[i] > data[i -1] and data[i] > data[i +1]:    #checking if idndex is greater then index before and after it
            print(i)

        elif data[i] > data[i + 1] and i == 0:      #checking if index 0 is a peak 
            print(i)

        else:
            continue

    if data[len(data) - 1] > data[len(data) - 2]:   #checking to see if last index is a peak by checking last index and compare it to seceond to last index
        print(len(data) - 1)
    
    


def valleys(data):
    data_len = len(data) - 1

    for i in range(0, data_len):        #pretty much same as above just reversed
        
        if data[i] < data[i -1] and data[i] < data[i +1]:
            print(i)

        elif data[i] < data[i + 1] and i == 0:
            print(i)

        else:
            continue

    if data[len(data) - 1] < data[len(data) - 2]:
        print(len(data) - 1)




def peaks_valleys(data):
    data_len = len(data) - 1

    for i in range(0, data_len):    #same as above
        
        if data[i] > data[i -1] and data[i] > data[i +1]: # same as above just twice as many elifs to cover all outcomes
            print(f"Peak at index {i}")

        elif data[i] > data[i + 1] and i == 0:
            print(f"Peak at index {i}")

        elif data[i] < data[i -1] and data[i] < data[i +1]:
            print(f"Valley at index {i}")

        elif data[i] < data[i + 1] and i == 0:
            print(f"Valley at index {i}")

        else:
            continue

    if data[len(data) - 1] < data[len(data) - 2]:
        print(f" Vally at index {len(data) - 1}")


    if data[len(data) - 1] > data[len(data) - 2]:
        print(f"Peak at index {len(data) - 1}")