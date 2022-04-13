n = int(input())
a = input()
b = input()
c = 0

print(sum(a[i]==b[i] for i in range(n)))