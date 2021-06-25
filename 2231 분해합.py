a = int(input())

for i in range(a):
    b = sum(map(int, str(i)))
    c = i + b
    
    if c == a:
        print(i)
        break
else:
    print("0")