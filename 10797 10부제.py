a = input()
b = [*map(str, input().split())]
if a in b:
    print(b.count(a))
else:
    print(0)