import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    stack.append(int(input().strip()))

max = 0
result = 0

for x in reversed(stack):
    if max < x:
        result += 1
        max = x

print(result)

# for _ in range(N):
#     a = int(input().strip())
#     if len(stack) == 0:
#         stack.append(a)
#     else:
#         if stack[-1] == a:
#             stack
#         elif stack[-1] > a:
#             stack.append(a)
#         else:
#             stack.pop()
#             stack.append(a)
# 같을 때 pop하고 더하고 ...코드 구현 진행중
