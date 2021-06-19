a = input()
b = int(input())
c = int(a[:-2] + '00')

while True:
    if c % b == 0:
        break
    c += 1
print(str(c)[-2:])