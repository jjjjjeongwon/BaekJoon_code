from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = list(map(int, input().split()))

queue = deque()

for i in range(N):
    queue.append(i+1)

print("<")
for i in range(N-1):
    for x in range(K-1):
        queue.append(queue.popleft())
    print(str(queue.popleft()))
    print(', ')
print(str(queue.popleft()))
print('>')
