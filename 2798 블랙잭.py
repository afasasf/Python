from itertools import permutations
n, m = map(int, input().split())
c = permutations([*map(int, input().split())],3)
ans = 0
for i in c:
    if m+1 > sum(i):ans = max(ans, sum(i))
print(ans)