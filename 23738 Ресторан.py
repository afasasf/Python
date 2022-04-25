a = input()
b = {'B':'v', 'E':'ye', 'H':'n', 'P':'r', 'C':'s', 'Y':'u', 'X':'h'}
c = ''
for i in a:
    if i in b:
        c += b[i]
    else:
        c += i.lower()
print(c)