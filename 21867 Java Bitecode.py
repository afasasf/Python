n = int(input())
a = input();b=""
for i in a:
    if i not in 'JAV':
        b+=i
if len(b) != 0:
    print(b)
else:
    print('nojava')