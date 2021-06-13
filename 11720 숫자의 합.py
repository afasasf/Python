a = int(input())
b = int(input())
c = b
d = 0

for i in range(a):
    e = int(c%10)
    c = int(c//10)
    d=d+e
print(d)