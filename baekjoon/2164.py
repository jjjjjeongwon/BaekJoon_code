from collections import deque
import sys
N = int(sys.stdin.readline())

queue = deque()

for i in range(N):
    queue.append(i+1)


for x in range(N-2):
    queue.popleft()
    val = queue.popleft()
    queue.append(val)


print(queue.pop())
