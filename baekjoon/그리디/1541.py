import sys
input = sys.stdin.readline

mathEx = input().strip().split('-')

numList = []
for i in range(0, len(mathEx)):
    a = mathEx[i].split('+')
    b = 0
    for j in a:
        b += int(j)
    numList.append(b)

n = numList[0]

for i in range(1, len(numList)):
    n -= numList[i]

print(n)
