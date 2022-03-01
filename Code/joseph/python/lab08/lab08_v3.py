#Lab 08 - Peaks and Valleys - Version 3 - Working

#Define and initialize list
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#define function pandv to determine peaks and valleys and size of pools
def pandv(data):
    p = []
    pv = []
    v = []
    vv = []
    #set the range to the first index and the penultimate index to exclude 0 and len(data)
    for index in range(1, len(data) - 1):
        #iterate through indices of data, append list p with any index that has a lower number on both sides
        if data[index + 1] < data[index] > data[index - 1]:
            p.append(index)
            #append list pv with the element value of the peak, this will give us the upper row of the pool
            pv.append(data[index])
        #iterate through indices of data, append list v with any index that has a higher number on both sides
        elif data[index + 1] > data[index] < data[index - 1]:
            v.append(index)
            #append ist vv with the element value of the valley, this will give us the bottom row of the pool
            vv.append(data[index])
    #compare the two lists, subtracting p from v to get the difference and add it to v to get the "other side"
    #of the tops of the pools.
    d = [v - p for v, p in zip(v, p)]
    o = [v + d for v, d in zip(v, d)]
    pools = [p for o in zip(p, o) for  p in o]
    #compare the number of peaks and valleys; if they are the same you can get the number of pools by halfing
    n_pools = int((len(p) + len(v)) / 2)
    #get the width of the pool x by counting the number of columns between p[x] and o[x] using range and subtracting 1
    w_pool = []
    #get the depth of the pool by counting the number of columns between pv[x] and vv[x]
    d_pool = []
    #calculate amount of water in each pool by multiplying the width by the depth and then subtracting 2*depth
    #to account for the "stairstep" nature of the x's.
    water_pool = []
    for x in range(n_pools):
        w_pool.append(len(range(p[x], o[x])) -1)
        d_pool.append(len(range(pv[x], vv[x], -1)))
        water_pool.append(((w_pool[x] * d_pool[x]) - (d_pool[x] * 2)))

    #iterate over the rows in the list, starting at the top, based on the max value in the list and working down with -1 step.
    #start with one space to match the 1st column of the list data and then iterate through the values in the list.
    #if the row value is greater than the list value, add a space and two spaces.  If the row value is the equal to or lower than
    #the list value, add an X and two spaces.  The two spaces ensure that the columns line up. Print the results of each row.
    #WATER
    #to add the water, we need to swap the order of the joining.  First add the X's then To add the water, we join a O if the
    #current row is in the range of the any pool we have identifed with vv and pv AND the data[i] is within the range of the pools identified in pools.

    print('\n'.join([' ' + '  '.join(['X' if row <= data[i] else 'O' if row in range(vv[0], pv[0] +1) and (i) in range(pools[0], pools[1]) else 'O'
    if row in range(vv[1], pv[1] +1) and (i) in range(pools[2], pools[3]) else ' ' for i in range(len(data))]) for row in range(max(data), 0 ,-1)]))
    #print the contents of the list 'data'
    print(data)
    #print the amount of water in each pool
    print('Starting with the highest pool as identified by peak:\n')
    for x in range(n_pools):
        print(f"pool number {x+1} has {water_pool[x]} units of water in it")

#    print(p, pv, v, vv, o, pools, w_pool, d_pool, water_pool)
pandv(data)