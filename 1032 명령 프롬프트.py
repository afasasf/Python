n=int(input())
a=[*input()]
for _ in range(n-1):
    b=[*input()]
    for j in range(len(a)):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))