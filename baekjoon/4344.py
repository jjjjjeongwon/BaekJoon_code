count = int(input())
ans = []

for x in range(count):
    a = list(map(int, input().split(" ")))
    ave = sum(a[1:])/a[0]

    c = 0
    for i in a[1:]:
        if i > ave:
            c += 1

    ans.append(round(c/a[0]*100, 3))

for i in ans:
    f = format(i, ".3f")
    print(str(f)+"%")
