# a = int(input())
# b = int(input())
# c = int(input())

# ans = str(a*b*c)

# for i in range(10):
#     print(ans.count(str(i)))


import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

print(str(A*B*C))

number_str = str(A*B*C)

for i in range(10):
    print(number_str.count(str(i)))
