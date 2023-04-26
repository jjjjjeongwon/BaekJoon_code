import heapq
from sys import maxsize
import sys
input = sys.stdin.readline

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

graph = [[] for i in range(N+1)]
cost = [maxsize] * (N+1)

for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))  # x도시에 (비용, 도착지)형태로 넣어줌

start, end = map(int, input().split())


def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))  # 비용과 시작점 heap에 추가
    cost[x] = 0  # 시작점은 비용이 0

    while pq:
        c, s = heapq.heappop(pq)  # 비용, 시작점 가져옴

        if cost[s] < c:  # 시작점에 해당하는 저장해뒀던 비용보다 새로운 비용이 크면 그냥 넘어감
            continue

        for nc, nd in graph[s]:  # 시작도시와 연결된 정보를 각각 가져옴 (비용, 도착지)
            newCost = c + nc  # 새로 저장할 비용은 비용+새도시의 비용

            if cost[nd] > newCost:  # 기존에 저장된 비용이 새로 저장된 비용보다 크면 갱신해준다.
                heapq.heappush(pq, (newCost, nd))  # 새로운 비용으로 push해준다
                cost[nd] = newCost


dijkstra(start)

print(cost[end])
