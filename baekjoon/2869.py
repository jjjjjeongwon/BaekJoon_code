a = list(map(int, input().split()))

day = a[0] - a[1]

if (a[2]-a[0] == 0):
    print(1)
else:
    if (a[2]-a[0]) % day == 0:
        print(1 + (a[2]-a[0])//day)
    else:
        print(2+(a[2]-a[0]) // day)
