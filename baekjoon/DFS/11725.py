import sys
sys.setrecursionlimit(200000)  # recursion error 뜨면 이거 세팅하기
input = sys.stdin.readline

N = int(input())

nodeParentList = [0] * (N+1)
graph = [[] for _ in range(N+1)]


for i in range(N-1):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)


def DFS(V):
    nodeParentList[1] = 1
    for i in graph[V]:

        if nodeParentList[i] == 0:
            nodeParentList[i] = V

            DFS(i)


DFS(1)

for i in range(2, N+1):
    print(nodeParentList[i])
