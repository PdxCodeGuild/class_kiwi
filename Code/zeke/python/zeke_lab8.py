# Lab 8: Peaks and Valleys
# Define the following functions:





# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# Visualization of test data:

# Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
# POI							P			V					P			V			
# Example I/O:

#                                                       X                 X
#                                                    X  X  X           X  X
#                               X                 X  X  X  X  X     X  X  X
#                            X  X  X           X  X  X  X  X  X  X  X  X  X
#                         X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
#                      X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#                   X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#                X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#             X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# >>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# >>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]
data_list = [
1,
2,
3,
4,
5,
6,
7,
6,
5,
4,
5,
6,
7,
8,
9,
8,
7,
6,
7,
8,
9,
]



'''
create two funcations Peak and Valley
loop over each position in list
check number before and after each number


'''
# 



# # peaks A peak has a lower number on both the left and the right.
# def peaks():
#     #     #len gives the length of a list without hardcode number
#      for i in range(len(data_list)):
#          if data_list[i -1] > data_list[i] < data_list[i +1]:
#              print("we found a peak")
# peaks()



# valleys A valley is a number with a higher number on both the left and the right.

def peak():
    list_of_peaks = []
    for i in range(len(data_list)):
        if i == 0 or i == len(data_list) -1:
            pass
        elif data_list[i -1] <data_list[i]> data_list[i +1]:
            list_of_peaks.append(i)

    return list_of_peaks
peak()


def valley():
    list_of_valley = []
    for i in range(len(data_list)):
        if i == 0 or i == len(data_list) -1:
            pass
        elif data_list[i-1] >data_list[i] < data_list[i +1]:
            list_of_valley.append(i)
    
    return list_of_valley
valley()

# peaks_and_valleys - uses the above two functions to compile 
# a single list of the peaks and valleys in order of appearance in the original data.
# def single_list():
def peaks_and_valleys(): 
    peaks = peak()
    valleys = valley()
    a = peaks + valleys
    a.sort()
    final_list = []
    for num in a:
        final_list.append(data_list[num])

    return final_list
   
        
    
    

print(peaks_and_valleys())



