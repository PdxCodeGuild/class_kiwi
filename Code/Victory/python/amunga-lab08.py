data =[1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
#index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def peaks(data):
    peak = []

    for index in range(1, len(data)-1):
        if data[index - 1] < data[index]> data[index + 1]:
            peak.append(index)
    
    return peak
print(peaks(data))

def valleys(data):
    valley = []

    for index in range(1, len(data)-1):
        if data[index - 1] > data[index]< data[index + 1]:
            valley.append(index)
    
    return valley

print(valleys(data))



def peaks_and_valleys(n):
    P=peaks(data)
    V=valleys(data)

    p_v = P + V

    p_v.sort()

    return p_v

print(peaks_and_valleys(data))

