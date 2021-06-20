a = int(input())

f = [0, 1]
for i in range(2, a+1):
    num = f[i-1] + f[i-2]
    f.append(num)
print(f[a])