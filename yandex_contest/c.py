import sys

n = int(sys.stdin.readline().strip())
int_array = [int(sys.stdin.readline().strip()) for _ in range(n)]

prev = int_array[0]
for i in int_array[1:]:
    if i != prev:
        print(i)
    prev = i
