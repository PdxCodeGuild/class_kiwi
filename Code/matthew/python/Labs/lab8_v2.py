
from xml.dom.minidom import Element
from lab8 import peaks, peaks_and_valleys, valleys

# --- Version 2


data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

# test = [1,2,3]

# for row in range(max(test),0, -1):
#     line = ''
#     for column in range(len(test)):
#         if row <= test[column]:
#             line += 'x '
#         else: 
#             line += '  ' 
#     print(line)

for row in range(max(data),0, -1):
    line = ''
    for column in range(len(data)):
        if row <= data[column]:
            line += ' x '
        # elif row >= data[column] and 14 < column <= 21:  # my attempt at Version 3.. It doesnt work
        #     line += ' o '
        # elif row >= data[column] and 7 <= column <= 12:
        #     line += ' o '
        else:
            line += '   '
    print(line)
print(data)

# print(peaks_and_valleys(data))
# print(len(data))