# VERSION 1


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    data_len = len(data) - 1

    for i in range(0, data_len):
        
        if data[i] > data[i -1] and data[i] > data[i +1]:
            print(i)

        elif data[i] > data[i + 1] and i == 0:
            print(i)

        else:
            continue

    if data[len(data) - 1] > data[len(data) - 2]:
        print(len(data) - 1)
    
    


def valleys(data):
    data_len = len(data) - 1

    for i in range(0, data_len):
        
        if data[i] < data[i -1] and data[i] < data[i +1]:
            print(i)

        elif data[i] < data[i + 1] and i == 0:
            print(i)

        else:
            continue

    if data[len(data) - 1] < data[len(data) - 2]:
        print(len(data) - 1)


peaks(data)

valleys(data)




# VERSION 2


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    data_len = len(data) - 1

    for i in range(0, data_len):
        
        if data[i] > data[i -1] and data[i] > data[i +1]:
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
    

peaks(data)

