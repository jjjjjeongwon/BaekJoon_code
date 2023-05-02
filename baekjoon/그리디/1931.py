import sys
input = sys.stdin.readline

N = int(input())
timetable = []

for i in range(N):
    s, e = list(map(int, input().split()))
    timetable.append([s, e])
timetable.sort(key=lambda x: (x[1], x[0]))

count = 0
lastEnd = 0
for i, j in timetable:
    if lastEnd <= i:
        count += 1
        lastEnd = j

print(count)
