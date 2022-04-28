from collections import Counter
a=[int(input())for _ in range(10)];a.sort()
b=Counter(a);c=b.most_common(1)
print(f'{int(sum(a)//10)}\n{c[0][0]}')