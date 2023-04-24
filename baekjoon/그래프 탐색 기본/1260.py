from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().strip().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a][b] = True  # 인접행렬에서 [a][b]와 [b][a]를 True로 바꿈
    graph[b][a] = True

visitedDFS = [False] * (N+1)  # false로 배열만들기
visitedBFS = [False] * (N+1)

# 큐


def BFS(V):
    q = deque([V])  # 큐에 시작 노드 넣음
    visitedBFS[V] = True  # visitedBFS배열의 V번째 True로 바꿈
    while q:  # q에 값이 있을 때만
        V = q.popleft()  # q의 왼쪽 값 꺼냄
        print(V, end=' ')  # 꺼낸값 print
        for i in range(1, N+1):  # 1부터 N까지 돈다
            # visited[i]가 False이고 graph[V][i]가 1이면 => 방문하지 않았으면서 연결이 되어 있다면
            if not visitedBFS[i] and graph[V][i]:
                q.append(i)  # q에 i추가
                visitedBFS[i] = True  # i번째도 True로 바꿈

# 재귀


def DFS(V):
    visitedDFS[V] = True  # 첫번째 탐색노드를 True로 바꿈
    print(V, end=' ')  # V 출력
    for i in range(1, N+1):  # 1에서 N까지 돈다
        if not visitedDFS[i] and graph[V][i]:  # 방문하지 않았으면서 인접행렬에서 연결이 되어 있다면
            DFS(i)  # i값으로 dfs를 돈다(깊이 탐색)


DFS(V)
print()
BFS(V)
