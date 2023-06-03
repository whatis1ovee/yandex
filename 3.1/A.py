"""n = int(input())
for i in range(n): 
    letter = input()
    if letter[0] not in ['а', 'б', 'в']:
        print('NO')
        break
else:
    print('YES')"""


n = int(input())
answer = "YES"
for i in range(n):
    letter = input()
    if letter[0] not in ['а', 'б', 'в']:
        
        answer = "NO"
        break

print(answer)