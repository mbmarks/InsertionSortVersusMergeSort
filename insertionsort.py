# keys is the list of numbers
def insertionsort(keys):
    for j in range(1,len(keys)):
        key = keys[j]
        i = j - 1
        while (i > -1 and keys[i] > key):
            keys[i+1] = keys[i]
            i = i - 1
        keys[i+1] = key
    return keys
