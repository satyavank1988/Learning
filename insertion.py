#!/usr/bin/python


def sorting(array):
    for index1 in range(1,len(array)):
        current = array[index1]
        index0 = index1 - 1
        while index0 >= 0 and array[index0] > current:
            array[index0 + 1] = array[index0]
            index0 = index0 - 1
        array[index0 + 1] = current

    return array


ar = [22,44,55,11,22,55,66,7,77,8,99,99,55,33,22,11,26,78]

print "before:",ar
print "after: ",sorting(ar)

