import sys
input = sys.stdin.readline

stack = []
stack_size = 0

a = input().strip()

for i in range(len(a)):
    stack.append(a[i])
    stack_size += 1
    # print(stack_size)
    print(stack)
    if stack[i-4:i] == ['P', 'P', 'A', 'P']:
        print(i)
