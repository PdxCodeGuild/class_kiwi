#Lab 08 - Peaks and Valleys - Version 1 - Working

#Define and initialize list
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#print the original list
print("the original list is: ", data, "\n")

#Define function peaks to return the indices of peaks; a peak has a lower number on left and right
def peaks():
    p = []
    #set the range to the first index and the penultimate index to exclude 0 and len(data)
    for index in range(1, len(data) - 1):
        #iterate through indices of data, append list p with any index that has a lower number on both sides
        if data[index + 1] < data[index] > data[index - 1]:
            p.append(index)
    return p

#define function valleys to return the indices of valleys; a valley has a high number on left and right
def valleys():
    v = []
    #set the range to the first index and the penultimate index to exclude 0 and len(data)
    for index in range(1, len(data) - 1):
        #iterate through indices of data, append list v with any index that has a higher number on both sides
        if data[index + 1] > data[index] < data[index - 1]:
            v.append(index)
    return v

#define function peaks_and_valleys to compile a single list of the peaks and valleys in order of appearance
def peaks_and_valleys(p, v):
    #merge the lists
    p_and_v = p + v
    #sort the lists
    p_and_v.sort()
    #return the sorted list
    return p_and_v


print(f"The peaks are: {peaks()}")
print(f"The valleys are: {valleys()}")

print(f"The peaks and valleys in order of appearance are: {peaks_and_valleys(peaks(),valleys())}")
