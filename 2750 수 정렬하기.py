a = int(input())
num = []

for _ in range(a):
    b = num.append(int(input()))

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

for n in num:
    print(n)