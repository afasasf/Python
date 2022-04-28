for _ in range(int(input())):
    cnt=0
    s = int(input())
    n = int(input())
    cnt += s

    for _ in range(n):
        q, p = map(int,input().split())
        cnt += q*p
    print(cnt)