def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)//2)
    print(mid)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    print(st, ed)
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1
        print("a[st], a[ed] ",a[st]," ", a[ed])

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

a = [2,3,5,1,4]
findZigZagSequence(a, len(a))



