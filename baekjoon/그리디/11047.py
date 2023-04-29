import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
coinList = [int(input()) for i in range(N)]
countCoin = 0

for i in range(N, 0, -1):
    if K // coinList[i-1] > 0:
        countCoin += K//coinList[i-1]
        K = K - (K//coinList[i-1])*coinList[i-1]
print(countCoin)
