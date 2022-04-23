import sys
for _ in range(3):
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for i in range(n)]

    if sum(a) == 0: print(0)
    elif sum(a) > 0: print('+')
    else: print('-')