a = []
cnt = 0
for i in range(5):
    a.append(sum([*map(int, input().split())]))

for j in a:
    cnt+=1
    if j == max(a):
        print(cnt,j)
        break