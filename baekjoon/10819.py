import sys
import itertools
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

nPrs = list(itertools.permutations(arr, n))

max_sum = 0

for nPr in nPrs:
    sum = 0
    for i in range(n-1):
        sum += abs(nPr[i]-nPr[i+1])
    if sum > max_sum:
        max_sum = sum

print(max_sum)
