from itertools import combinations
n, m = map(int, input().split())
a = combinations(range(1, n+1),m)
for i in a:
    print(' '.join(map(str, i)))