for _ in ' '*int(input()):
    a,b=input().split()
    a=int(a)
    print(b[:a-1]+b[a:])