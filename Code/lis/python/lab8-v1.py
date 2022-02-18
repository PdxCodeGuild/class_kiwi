# Lab 8 Version 1  Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
 
def peaks(data):

      peaks = []

      for i, v in enumerate(data[0:-1]):
         if v > data[i - 1] and v > data[i + 1]:
            peaks.append(i)
      return peaks

print("Peaks: ", peaks(data))


def valleys(data):

   # a good place to try list comprehensions and compare with peaks function, but too complicated... 
   valleys_enum = [(i,v) for i,v in enumerate(data[0:-1]) if v < data[i - 1] and v < data[i + 1]]
   valleys = ([i[0] for i in valleys_enum][1::])
   return (valleys)

print("Valleys: ", valleys(data))


def peaks_and_valleys(data):
   
   peaks_and_valleys = peaks(data) + valleys(data)
   return sorted(peaks_and_valleys)

print("Peaks and Valleys: ", peaks_and_valleys(data))