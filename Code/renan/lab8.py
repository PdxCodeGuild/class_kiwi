
#                           P                                   P
data = [1,	2,	3,	4,	5,	6,	7,	6,	5,	4,	5,	6,	7,	8,	9,	8,	7,	6,	7,	8,	9]
#       0 , 1,  2,  3,  4,  5,  6,  7,  8,  9,
#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data):
    peak_indices = []   
    #loop over data (1:-1 keeps the loop between index 2 and 8 for the peaks n valleys...to analyze left and right..)
    for i in range(1, len(data) -1):
        # compare current index with previous and next values
        next = data[i + 1]
        previous = data[i -1]
        current = data[i]
        #if previous and next are both lower value than current, we found a peak
        if previous < current > next:
            
            peak_indices.append(i)
    
    return peak_indices

print("Found A Peak")  
  
# print(peaks())

#valleys - return the indices of valleys.
def valleys():
    valley_indices = []
    
    for i in range(1, len(data) -1):
        
        if data[i- 1] > data[i] < data[i +1]: 
            valley_indices.append(i)    

    # if(value[data] < value[data-1] and value[data] < value[data + 1]):
    #     print
    # 
    return valley_indices

print(peaks(data))
print(valleys())




def peaks_and_valleys():
    p_indices = peaks(data)
    v_indices = valleys()
    
    peaks_valleys = p_indices + v_indices
    
    peaks_valleys.sort()
    return peaks_valleys

def print_peaks_and_valleys():
    rows = max(data)
    cols = len(data)
    for i in range(rows, 0, -1):
        for j in range(cols):
            if i > data[j]:
                print(' ', end=" ")
            else:
                print('X', end=" ")
        print()    
            
    print(data)
    
print_peaks_and_valleys()
