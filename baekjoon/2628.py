square = list(map(int, input().split()))
n = int(input())
width = [square[0], 0]
height = [square[1], 0]

for _ in range(n):
    a = list(map(int, input().split()))
    # input()안에 값이 같이 반복되어 찍혀나옴
    if a[0] == 0:
        height.append(a[1])
    else:
        width.append(a[1])

width.sort(reverse=True)
height.sort(reverse=True)


wdt = []
hgt = []

for x in range(len(width)-1):
    wdt.append(width[x]-width[x+1])

for x in range(len(height)-1):
    hgt.append(height[x]-height[x+1])


print(max(wdt)*max(hgt))
