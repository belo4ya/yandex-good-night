import sys
import pprint


def readline():
    return sys.stdin.readline().strip()


def distance_2d(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n = int(readline())
cities = [tuple(map(int, readline().split())) for _ in range(n)]
k = int(readline())
start, end = map(int, readline().split())

print(n)
print(cities)
print(k)
print(start, end)

graph = [[distance_2d(start_city, end_city) for end_city in cities] for start_city in cities]
pprint.pprint(graph)

print(graph)
print(graph[start][end])
