import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def DFS(V, group):
    visited[V] = group
    for i in graph[V]:
        if visited[i] == 0:  # 방문안했으면
            if not DFS(i, -group):  # 인접한 노드가 1, -1 이런식이 아니라면
                return False
        elif visited[i] == visited[V]:  # 방문했는데, 둘 사이에 그룹이 같으면(1,1) or (-1, -1)
            return False
    return True


for _ in range(int(input())):  # 테케 개수만큼 돈다
    V, E = map(int, input().split())  # 첫 줄에 나오는 Vertex, Edge 개수 받아오기
    graph = [[] for i in range(V+1)]  # 정점 개수보다 1개 많게 그래프 배열 생성
    visited = [0] * (V+1)  # 방문 여부 배열 [0, 0, 0, ...] 이런식으로 정점개수 보다 1개 많게 생성

    for i in range(E):  # 간선 정보 저장(간선 개수만큼 돌면서)
        X, Y = map(int, input().split())
        graph[X].append(Y)
        graph[Y].append(X)

    bipartite = True  # 변수생성 및 True로 초기화

    for i in range(1, V+1):  # 정점만큼 돈다
        if visited[i] == 0:  # 방문 안했으면
            bipartite = DFS(i, 1)  # DFS로 (i, group==1초기값으로 두고) 수행
            if not bipartite:  # bipartite가 False면
                break  # 나간다

    print('YES' if bipartite else 'NO')
