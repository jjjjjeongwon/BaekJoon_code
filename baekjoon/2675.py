i = int(input())

for x in range(i):
    a = input().split(" ")
    ans = []
    for x in a[1]:
        ans.append(int(a[0])*x)
    print("".join(ans))
