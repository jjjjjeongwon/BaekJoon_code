import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())


def S(k):
    if k == 0:
        return "moo"
    return S(k-1)+"m"+"o"*(k+2)+S(k-1)


start = 1
end = N
answer = 0

while start < end:
    mid = (start+end)//2

    if len(S(mid)) < N:
        start = mid + 1

    else:
        end = mid - 1
        answer = mid-1
print(S(answer)[N-1])
