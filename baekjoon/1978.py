a = int(input())

numbers = list(map(int, input().split()))

ans = 0

for _ in range(a):  # [1,3,5,7]
    cnt = 0
    for x in range(2, numbers[_]+1):
        if numbers[_] % x == 0:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)
