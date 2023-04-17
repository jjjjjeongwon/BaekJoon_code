from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
queue = deque()

for i in range(N):
    command = input().strip().split()

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            # val = queue.popleft()
            # print(val)
            # queue.appendleft(val)
            print(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            val = queue.pop()
            print(val)
            queue.append(val)
# queue[-1]로 처리하면 안됨
    elif command[0] == "size":
        print(len(queue))
