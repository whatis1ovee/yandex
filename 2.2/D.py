v_1 = int(input())
v_2 = int(input())
v_3 = int(input())
v_max = max(v_1, v_2, v_3)
v_min = min(v_1, v_2, v_3)
if v_max == v_1:
    print('1. Петя')
elif v_max == v_2:
    print('1. Вася')
elif v_max == v_3:
    print('1. Толя')
if v_1 != v_max and v_1 != v_min:
    print('2. Петя')
elif v_2 != v_max and v_2 != v_min:
    print('2. Вася')
elif v_3 != v_max and v_3 != v_min:
    print('2. Толя')
if v_min == v_1:
    print('3. Петя')
elif v_min == v_2:
    print('3. Вася')
elif v_min == v_3:
    print('3. Толя')
