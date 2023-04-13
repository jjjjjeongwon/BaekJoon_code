import sys
input = sys.stdin.readline

N = input().strip()
fix_N = N
count = 0

if len(N) == 1:
    N = "0" + N

while True:
    if int(N[0])+int(N[1]) < 10:
        N = N[1] + str(int(N[0])+int(N[1]))
        count += 1
        if int(fix_N) == int(N):
            break
    else:
        N = N[1] + str((int(N[0])+int(N[1])))[1]
        count += 1
        if int(fix_N) == int(N):
            break
print(count)
