# Sample Input
# 07:05:45PM

# Sample Output
# 19:05:45

# def timeFormatChange(s):
#     l = s.split(":")
#     t = l[len(l)-1]
#     t = t[2] + t[3]
#     l[len(l)-1] = l[len(l)-1][0] + l[len(l)-1][1]
#     if t == "PM":
#         l[0] = int(l[0])+12
#     else:
#         if l[0] == "12":
#             l[0] = "00"
#     s = str(l[0])+":"+l[1]+":"+l[2]
#     print(s)
#     #return f"{h:02}{msec}"


def timeFormatChange(s):
    x = ''
    hr = s[:2]
    t = s[-2] + s[-1]
    if t == "PM": 
        hr=str(int(hr)+12)
    else:
        if hr == '12':
            hr = '00'
    x = hr+s[2:len(s)-2]
    print(x)

timeFormatChange('01:05:45AM')