a = input().upper()
b = list(set(a))
cnt = []
for i in b:
    c = a.count(i)
    cnt.append(c)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    max_index = cnt.index(max(cnt))
    print(b[max_index])