# a = int(input())

# for x in range(a):
#     b = list(input())

#     count = 0
#     sum_count = 0
#     for x in b:
#         if x == 'O':
#             count += 1
#             sum_count += count
#         else:
#             count = 0
#     print(sum_count)


import sys

n = int(sys.stdin.readline())


for _ in range(n):
    count = 0
    score = 0
    ox = list(sys.stdin.readline().strip())
    for i in range(len(ox)):
        if ox[i] == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
