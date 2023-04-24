import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 정점, 간선

graph = [[] for _ in range(N+1)]  # 정점마다 배열 생성 [[], [], [], ...]
visited = [False] * (N+1)  # 정점만큼 방문여부 배열 생성

for i in range(M):  # 간선만큼 돌면서 간선 정보가 담긴 배열 생성
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)


def DFS(V):
    visited[V] = True  # 초기값을 visited배열에서 True로 변경
    for i in graph[V]:  # 배열을 돈다 (ex. 1번 배열은 => [2, 5])
        if visited[i] == False:  # 체크하지 않은 연결된 노드를 True로 바꿈
            visited[i] = True
            DFS(i)  # 반복


count = 0
for i in range(1, N+1):  # 정점만큼 다 방문했는지 확인하고 , 다 안했다면 count를 올리고 DFS()반복
    if visited[i] == False:
        count += 1
        DFS(i)

print(count)
