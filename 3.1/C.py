d = int(input())
n = int(input())
for i in range(n):
    s = input()
    if len(s) <= d:
        print(s)
    else:
        print(s[:d - 3] + '...')
