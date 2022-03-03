data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

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





def peaks_and_valleys(peaks, valleys):
    all_peaks_and_valleys = peaks + valleys
    all_peaks_and_valleys.sort()

    return all_peaks_and_valleys


def print_peaks_and_valleys(data):
    rows = max(data)
    columns = len(data)
    for i in range(rows, 0, -1):
        for j in range(columns):
            if i > data[j]:
                print('  ', end=' ')
            else:
                print(' x', end=' ')
        print()
    print(data)


all_peaks = peaks(data)
print(all_peaks)

all_valleys = valleys(data)
print(all_valleys)

all_peaks_and_valleys = peaks_and_valleys(all_peaks, all_valleys)
print(all_peaks_and_valleys)

print_peaks_and_valleys(data)