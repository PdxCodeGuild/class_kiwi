data = [1, 2 , 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]     #peaks and valleys list


def peaks(data):                                                           
    for index, number in enumerate(data):
        if index == 0 or index == len(data) -1:                     #not running first index or last
            continue
        
        elif number > data[index -1 ] and number > data[index + 1]: #checking if index before or after is less then number
            print(index)
  
def valleys(data):                                                  
    for index, number in enumerate(data):
        if index == 0 or index == len(data) -1:                     
            continue
        
        elif number < data[index -1 ] and number < data[index + 1]:  ##checking if index before or after is greater then number
            print(index)
            
def peaks_valleys(data):
    for index, number in enumerate(data):
        if index == 0 or index == len(data) -1:
            continue
        
        elif number > data[index -1 ] and number > data[index + 1]:
            print(index)
        
        elif number < data[index -1 ] and number < data[index + 1]:
            print(index)
            
peaks_valleys(data)


"""
Lab 8: Peaks and Valleys
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
""" 

