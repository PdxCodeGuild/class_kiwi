'''         +-+#^#+--+#^#+--+#^#+-+             
           Project: Peaks and Valleys             ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/15/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''




from asyncio import DatagramProtocol


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


# From the lab review
def draw_peaks_valleys(data):
    """Draws peaks and valleys of a list"""
    rows = max(data)
    cols = len(data)
    for i in range(rows, 0, -1):
        for num in range(cols):
            if i > data[num]:
                print("  ", end=" ")
            else:
                print(" X", end=" ")
        print()
    print(data)
        
    return

def draw_peaks_valleys_with_water(data):
    """Draws peaks and valleys of a list"""
    rows = max(data)
    cols = len(data)
    pvs = peaks_and_valleys(data)
    for i in range(rows, 0, -1):
        for num in range(cols):
            if i > data[num]:
                print("  ", end=" ")
           
            else:
                for i in range(len(pvs) - 1):
                    current = pvs[i]
                    next = pvs[i+1]

                
                    if current > num < next:
                        print(" O", end=" ")
                print(" X", end=" ")
        print()
    print(data)
        
    return


def main():

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    print(peaks(data), "Indices of Peaks")
    print(valleys(data), "Indices of Valleys")
    print(peaks_and_valleys(data),"Values of Peaks, and Valleys in order")
    draw_peaks_valleys(data)
    draw_peaks_valleys_with_water(data)

if __name__ == "__main__":
    main()


