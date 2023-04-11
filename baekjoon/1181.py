import sys
input = sys.stdin.readline

i = int(input())

words = list({input().rstrip() for _ in range(i)})

words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
