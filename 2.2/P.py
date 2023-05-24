v_1 = int(input())
v_2 = int(input())
v_3 = int(input())
v_max = max(v_1, v_2, v_3)
v_min = min(v_1, v_2, v_3)
line_1 = 0
line_2 = 0
line_3 = 0
line_4 = ('   II      I      III   ')

if v_max == v_1:
    line_1 = ('          Петя          ')
elif v_max == v_2:
    line_1 = ('          Вася          ')
elif v_max == v_3:
    line_1 = ('          Толя          ')

if v_1 != v_max and v_1 != v_min:
    line_2 = ('  Петя  ')
elif v_2 != v_max and v_2 != v_min:
    line_2 = ('  Вася  ')
elif v_3 != v_max and v_3 != v_min:
    line_2 = ('  Толя  ')

if v_min == v_1:
    line_3 = ('                  Петя  ')
elif v_min == v_2:
    line_3 = ('                  Вася  ')
elif v_min == v_3:
    line_3 = ('                  Толя  ')

print(line_1)
print(line_2)
print(line_3)
print(line_4)
