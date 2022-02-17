#Lab 08 - Peaks and Valleys - Version 2 - Working

#Define and initialize list
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#iterate over the rows in the list, starting at the top, based on the max value in the list and working down with -1 step.
#start with one space to match the 1st column of the list data and then iterate through the values in the list.
#if the row value is greater than the list value, add a space and two spaces.  If the row value is the equal to or lower than
#the list value, add an X and two spaces.  The two spaces ensure that the columns line up. Print the results of each row.
print('\n'.join([' ' + '  '.join([' ' if row > data[i] else 'X' for i in range(len(data))]) for row in range(max(data), 0 ,-1)]))

#print the contents of the list 'data'
print(data)