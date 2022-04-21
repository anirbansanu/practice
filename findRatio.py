#Find ratio of zeroes, positive numbers and negative numbers in the Array

def findRatio(arr):
    zero = 0
    positive = 0
    negative = 0
    length = len(arr) 
    for item in arr:
        if item == 0:
            zero += 1
        elif item > 0:
            positive += 1
        elif item < 0:
            negative += 1
    return zero/length,positive/length,negative/length
arr = [-2,4,-1,5,0,-8]

print(findRatio(arr))