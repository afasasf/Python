import sys;a, b = map(int, sys.stdin.readline().split())
print((abs(a-b)+1)*(a+b)//2)