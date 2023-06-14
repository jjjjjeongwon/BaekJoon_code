import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    lst = [0]*(n+1)
    for _ in range(n):
        a, b = map(int, input().split())
        lst[a] = b

    ans = 1
    second_max = lst[1]
    for i in range(2, n+1):
        if lst[i] < second_max:
            second_max = lst[i]
            ans += 1
    print(ans)
