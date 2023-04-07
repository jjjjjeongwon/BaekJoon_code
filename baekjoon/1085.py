a, b, c, d = map(int, input().split())

numbers = [a, b, c-a, d-b]
print(min(numbers))
