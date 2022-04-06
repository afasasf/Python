t = int(input())
a = b = 0
v = input()
a = v.count('A')
b = v.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
