a = int(input())
b = list(map(int, input().split()))
m = max(b)
re = 0

for i in range(0, a):
    b[i] = b[i]/m*100
    re = re + b[i]
    
re = re/a
print(re)