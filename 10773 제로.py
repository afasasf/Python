a = []
for _ in range(int(input())):
    b = int(input())

    if b == 0:
        a.pop() 
    else:
        a.append(b)
print(sum(a))