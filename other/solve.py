a = int(input())
b = int(input())
c = int(input())

if a == 0 and b == c * c:
    print('MANY SOLUTIONS')
elif a == 0 or c < 0:
    print('NO SOLUTION')
else:
    x = int((c * c - b) / a)
    if a * x + b == c * c:
        print(x)
    else:
        print('NO SOLUTION')
