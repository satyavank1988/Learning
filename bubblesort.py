
import random


def bubbleSort1(arr):
    print "\n Unsorted array"
    print arr
    arrLength = len(arr)
    for num in range(arrLength):
        for i in range(0,arrLength-num-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    # printning sorted array
    print "After sorting"
    print arr

def arrFormation(arrLength):
    arr = []
    for i in range(num):
        arr.append(random.randint(0,1000))
    return arr

def bubbleSort2(arr):
    print "\n Unsorted array\n", arr
    for num in range(len(arr)-1,0,-1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] =  arr[i+1], arr[i]

    print "\n Sorted array"
    print arr

def arrays(num):
    arr1 = arrFormation(num)
    arr2 = arrFormation(num)
    print "Sorting method1\n"
    bubbleSort1(arr1)
    print "Sorting method 2:\n"
    bubbleSort2(arr2)


num = input("Enter the lenght of array : ")

arrays(num)

