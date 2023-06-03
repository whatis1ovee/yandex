'''n = int(input())
count = 0
for i in range(n):
    s = input()
    count += s.count('зайка')
print(count)'''

n = int(input())
count_zaika_all_text = 0
for i in range(n):
    s = input()
    count_zaika_stroka = s.count('зайка')
    count_zaika_all_text += count_zaika_stroka
    
print(count_zaika_all_text)
