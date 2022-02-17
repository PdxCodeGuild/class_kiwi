'''         +-+#^#+--+#^#+--+#^#+-+             
           Project: Peaks and Valleys             ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/15/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''




def peaks(data):
    """Gets peaks in a list"""
  
    for i, num in enumerate(data):
        try:
            if data[i] > data[i+1] and data[i] > data[i-1]:
                if data[i-1] == data[-1]:
                    continue
                print("index", i, ':', num)
                print("peaks")
        except IndexError:
            continue

    return




def valleys(data):
    """Gets valleys in a list"""

    for i, num in enumerate(data):
        try:
            if data[i] < data[i+1] and data[i] < data[i-1]: # data[i-1] is looping back to the last position 
                if data[i-1] == data[-1]:
                    continue
                print(data[i-1])
                print("index", i, ':', num)
                print("valleys")
        except IndexError:
            continue
    return




def peaks_and_valleys(data):
    """Gets peaks and valleys of a list"""
    list = []
    for i, num in enumerate(data):
        try:
            if data[i] > data[i+1] and data[i] > data[i-1]:
                if data[i-1] == data[-1]:
                    continue
                list.append(num)
                
            elif data[i] < data[i+1] and data[i] < data[i-1]:
                if data[i-1] == data[-1]:
                    continue
                list.append(num)
                
            
        except IndexError:
            continue

    return list
# Ignore for now
def draw_peaks_valleys(data):
    for num in data:
        if num == 1:
            print("""
X""")
        if num == 2:
            print("""
 X
 X""", end="")
    return



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks(data)
valleys(data)
print(peaks_and_valleys(data))



