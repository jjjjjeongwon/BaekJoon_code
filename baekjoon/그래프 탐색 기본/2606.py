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
    for i in graph[V]:  # graph[1] 배열부터 탐색해서 i가 false면, true로 바꿔주고 count를 1더한다
        if visited[i] == False:
            visited[i] = True
            count += 1  # 1은 제외하고 그 다음부터 count되기 때문에 count에서 1빼는 방식 아님
            DFS(i)  # i 다시 탐색
    return


DFS(1)
print(count)
