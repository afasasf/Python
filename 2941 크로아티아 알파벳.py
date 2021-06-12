a = input()
b = ['c=','c-','dz=','d-','lj','nj','s=','z=']
c = 0

for i in b:
    if i in a:
        a = a.replace(i," ")
print(len(a))