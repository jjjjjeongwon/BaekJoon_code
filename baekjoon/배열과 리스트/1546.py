import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
scoreMax = max(score)

updateAverage = 0

for i in range(N):
    updateAverage += score[i]*100/scoreMax

print(updateAverage/N)
