k = int(input())
n = int(input())
if n > 0:
    for i in range(k, n, 1):
        print(i)
else:
    for i in range(k, n - 1, -1):
        print(i)
