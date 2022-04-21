# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9 
# The left-to-right diagonal = 1+5+9 = 15. 
# The right to left diagonal = 3+5+9 = 17. 
# Their absolute difference is 15 - 17 = 2.
 
def diagonalDifference(arr):
    i = 0 
    j = len(arr)
    rtol = 0
    ltor = 0
    while i < j:
        rtol = rtol + arr[i][i]
        ltor = ltor + arr[i][j-i-1]
        i+=1
    print('Right TO Left : ',rtol)
    print('Left TO Right : ',ltor)
    return abs(rtol - ltor) 

a = [[1,2,3],[4,5,6],[9,8,9]]
print(diagonalDifference(a))
