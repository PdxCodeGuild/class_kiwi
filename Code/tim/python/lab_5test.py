




def lotto_check(lotto_list,player_list):
    lotto_count = 0
    for i in range(len(lotto_list)):
        if lotto_list[i] == player_list[i]:
            lotto_count += 1
    return lotto_count
        


# list_1 = [45, 23, 68] 
# list_2 = [23, 45, 68]
# count = lotto_check(list_1,list_2)

# print(count)