from math import gcd, lcm
t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    print(lcm(a, b))