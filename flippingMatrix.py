def flippingMatrixColumn(m,col):
    i = 0 
    j = col 
    temp = [] 
    try:
        while i < len(m):
            temp.append(m[i][j])
            i+=1
        while i > 0:
            m[j-i+1][j]=int(temp[i-1])
            i-=1
    except:
        print("Matrix Len Out Of Range")
    return m

def flippingMatrixRow(m,row):
    try:
        m[row] = m[0][::-1]
    except:
        print("Matrix Len Out Of Range")
    return m

if __name__ == '__main__':
    m = [[1,2,3],[4,5,6],[7,8,9]]
    m = flippingMatrixColumn(m,2)
    print(m)
    m = flippingMatrixRow(m,0)
    print(m)