#lab 8 peaks and valleys

#define the data
data = [
    1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9
]

# create the peaks function
# identify data being greater or lesser than its neighbor
# peaks
peaks = []
for i in range(1, len(data)-1): 
    if data[i - 1] < data[i] > data[i + 1]:
        peaks.append(i)
    else:
        continue
print(f'>>> peaks \n{peaks}')
          
#valleys
valleys = []
for i in range(1, len(data)-1): 
    if data[i - 1] > data[i] < data[i + 1]:
        valleys.append(i)
    else:
        continue
print(f'>>> valleys \n{valleys}')

peaks_and_valleys = peaks + valleys
peaks_and_valleys.sort()
print(f'>>> peaks and valleys \n{peaks_and_valleys}')