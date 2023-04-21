import heapq
import sys
input = sys.stdin.readline
N = int(input())

max_heap = []
min_heap = []

for i in range(N):
    a = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-a, a))
    else:
        heapq.heappush(min_heap, a)

    if max_heap and min_heap and max_heap[0][1] > min_heap[0]:
        val_max = heapq.heappop(max_heap)[1]
        val_min = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-val_min, val_min))
        heapq.heappush(min_heap, val_max)
    print(max_heap[0][1])
