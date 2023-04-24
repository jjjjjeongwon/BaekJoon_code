import sys
input = sys.stdin.readline

N = int(input())
M = int(input())


graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)


for i in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)

count = 0


def DFS(V):
    global count
    visited[V] = True
    for i in graph[V]:
        if visited[i] == False:
            visited[i] = True
            count += 1
            DFS(i)
    return


DFS(1)
print(count)
