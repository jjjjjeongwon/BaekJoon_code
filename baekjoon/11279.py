import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    a = int(input())
    if a == 0:
        if heap:
            print(-1 * (heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap, -a)
