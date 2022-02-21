data =[1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def peaks(n):

    for x in n:
        if data[x-1]< data[x] > data[x+1]:
            return [data[x],index[x]]
            
P=peaks(data)

def valleys(m):

    for y in m:

        if data[y-1]> data[y] <data[y+1]:
            return [index[y], data[y]]

V=valleys(data)

print(P)
print(V)


def peaks_and_valleys(n):

    
    for z in range(len(n)):
        w = [P[z],V[z],P[z+1],V[z+1]]
        return w

print(peaks_and_valleys(data))


