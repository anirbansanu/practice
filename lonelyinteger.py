# input : arr = [1,2,3,4,4,3,2,5,1]
# output : 5
def lonelyinteger(arr):
    d={} 
    for i in range(len(arr)):
        try:
            d[arr[i]] = d.get(arr[i]) + 1
        except:
            d[arr[i]] = 1
    s=''
    for i in d.keys():
        if d[i] == 1:
            s += str(i)
    return s

if __name__ == '__main__':
    print(lonelyinteger([1,2,3,4,5,3,2,1]))