from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append([0] * N)

print(graph)

K = int(input())

for _ in range(K):
    graph.append([0] * N)


# for i in range(K):
#     a, b = map(int, input().split())
