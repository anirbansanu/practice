# Print two space-separated integers on one line: 
# the minimum sum and the maximum sum of elements.
# Input
# [1,2,3,4,5]
# Output
# 10 -> min  
# 14 -> max

def maxAndMinFromArrSum(arr):
    max = 0
    min = 99999
    sum = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if j == i:
                continue
            sum = sum + arr[j]
        if max < sum:
            max = sum
        if min > sum:
            min = sum
        sum = 0
    print(min," ",max)

maxAndMinFromArrSum([1,2,3,4,5])