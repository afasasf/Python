a = input()
x = ''
for i in a:
    if i.isupper():
        i=i.lower()
    elif i.islower():
        i=i.upper()
    x+=i
print(x)