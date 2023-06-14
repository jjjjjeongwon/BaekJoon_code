import sys

n = int(input())
N = list(input())
answer = 0

for i in range(n):
    answer += int(N[i])

print(answer)
