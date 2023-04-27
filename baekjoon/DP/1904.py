import sys
input = sys.stdin.readline

N = int(input())

binaryList = [-1] * (N+1)  # 자연수 크기+1만큼 배열 생성


binaryList[0] = 1
binaryList[1] = 2

for i in range(2, N+1):
    binaryList[i] = (binaryList[i-1] + binaryList[i-2]) % 15746

print(binaryList[N-1])
