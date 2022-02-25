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
    list = []
    for i, num in enumerate(data):
        try:
            if data[i] > data[i+1] and data[i] > data[i-1]:
                if data[i-1] == data[-1]:
                    continue
                list.append(i)
        except IndexError:
            continue

    return list




def valleys(data):
    """Gets valleys in a list"""
    list = []
    for i, num in enumerate(data):
        try:
            if data[i] < data[i+1] and data[i] < data[i-1]: # data[i-1] is looping back to the last position 
                if data[i-1] == data[-1]:
                    continue
                list.append(i)
        except IndexError:
            continue
    return list




def peaks_and_valleys(data):
    """Gets peaks and valleys of a list and returns a list"""
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
    pictoral = []
    o = ''
    for i, num in enumerate(data):
        for i in range(num):
            print("X")
        

        
        
            
      
            

    return o


def main():

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    print(peaks(data), "Indices of Peaks")
    print(valleys(data), "Indices of Valleys")
    print(peaks_and_valleys(data),"Values of Peaks, and Valleys in order")
    print(draw_peaks_valleys(data))


if __name__ == "__main__":
    main()


