def peaks(data):
    all_peaks = []
    for i in range(1, len(data) - 1):
        if data[i + 1] < data[i] > data[i - 1]:
            all_peaks.append(i)
    return all_peaks



def valleys(data):
    all_valleys = []
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i] < data[i - 1]:
            all_valleys.append(i)

    return all_valleys





def peaks_and_valleys(data):
    all_peaks_and_valleys = []
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i] < data[i - 1] or data[i + 1] < data[i] > data[i - 1]:
            all_peaks_and_valleys.append(i)

    return all_peaks_and_valleys




data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


all_peaks = peaks(data)
print(all_peaks)

all_valleys = valleys(data)
print(all_valleys)

all_peaks_and_valleys = peaks_and_valleys(data)
print(all_peaks_and_valleys)