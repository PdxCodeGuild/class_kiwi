# # Lab 8: Peaks and Valleys

# Define the following functions:
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


# 1. `peaks` - Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data: list[int]) -> list:
    n = len(data)
    peaks_list = []
    for i in range (0, n):
        if i == n-1:
            pass 
        elif data[i] > data [i+1] and data[i] > data[i - 1]:
            peaks_list.append(i)
    return peaks_list
    

print(peaks(data))

# 1. `valleys` - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

def valleys(data: list[int]) -> list:
    n = len(data)
    valleys_list =[]
    for i in range (0, n):
        if i ==n-1:
            pass
        elif i == 0:
            pass 
        elif data[i] < data [i+1] and data[i] < data[i - 1]:
            valleys_list.append(i)
    return valleys_list

print(valleys(data))

# 1. `peaks_and_valleys` - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
peaks_and_valleys = peaks(data) + valleys(data)
peaks_and_valleys.sort()
print(peaks_and_valleys)
# Visualization of test data:

# | Data    |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 | 9 | 8 | 7 | 6 | 7 | 8 | 9 |
# |---------|----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
# | Index   |  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
# | POI     |    |   |   |   |   |   | P |   |   | V |   |   |   |   | P |   |   | V |   |   |   |


# Example I/O:
# ```python
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
# ```


# ## Version 2 (optional)

# Using the `data` list above, draw the image of `X`'s above.

# ## Version 3 (optional)

# Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by `O`'s. Given `data`, calculate the amount of water that would be collected.

# ```
#                                                   X  O  O  O  O  O  X
#                                                X  X  X  O  O  O  X  X
#                           X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
#                        X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
#                     X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
#                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#         X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

