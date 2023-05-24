t_1 = int(input())
t_2 = int(input())
t_3 = int(input())
if t_1 < (t_2 + t_3) and t_2 < (t_1 + t_3) and t_3 < (t_1 + t_2):
    print("YES")
else:
    print("NO")
