import sys

j = sys.stdin.readline().strip()  # драгоценности
s = sys.stdin.readline().strip()  # камни

result = 0
for symbol in s:
    if symbol in j:
        result += 1

print(result)
