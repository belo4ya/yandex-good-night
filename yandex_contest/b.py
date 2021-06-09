import sys

n = int(sys.stdin.readline().strip())
vec = [int(sys.stdin.readline().strip()) for _ in range(n)]

counter = 0
max_value = 0
for el in vec:
    if el == 1:
        counter += 1
        max_value = max(max_value, counter)
    else:
        counter = 0

print(max_value)
