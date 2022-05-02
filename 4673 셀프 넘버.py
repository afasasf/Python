a,b=set(range(1,10001)),set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    b.add(i)
for i in sorted(a-b):
    print(i)
