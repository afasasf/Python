import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
for i in sorted(a, reverse=True):
    print("할카스")