import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 시간초과 =>
# numList = list(map(int, input().split()))

# for i in range(M):
#     start, end = map(int, input().split())
#     print(sum(numList[start-1:end]))

numList = list(map(int, input().split()))
addList = [0]
sumValue = 0

for i in range(N):
    sumValue += numList[i]
    addList.append(sumValue)

for j in range(M):
    start, end = map(int, input().split())
    print(addList[end]-addList[start-1])
