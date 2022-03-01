# Lab 8: Peaks and Valleys
# Version 1

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valley_list = []
p_v_list = []


def peak(data):
    for i in range(1, len(data) - 1):
        left = data[i - 1]
        middle = data[i]
        right = data[i + 1]
        if middle > right and middle > left:
            peak_list.append(i)
    return peak_list


def valley(data):
    for i in range(1, len(data) - 1):
        left = data[i - 1]
        middle = data[i]
        right = data[i + 1]
        if middle < right and middle < left:
            valley_list.append(i)
    return valley_list


def p_v(data):
    for i in range(1, len(data) - 1):
        left = data[i - 1]
        middle = data[i]
        right = data[i + 1]
        if middle > right and middle > left:
            p_v_list.append(i)
        if middle < right and middle < left:
            p_v_list.append(i)

    return p_v_list


print(peak(data))
print(valley(data))
print(p_v(data))
