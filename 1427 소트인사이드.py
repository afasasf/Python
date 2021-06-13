a = int(input())
b = []
b = list(map(int, str(a)))
b.sort(reverse=True)

for i in b:
    print(i, end="")