a, b = map(int, input().split())

for x in map(int, input().split()):
    if x < b:
        print(x, end=" ")
