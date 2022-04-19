a = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    b = input()
    if b == '#':
        break
    c = 0
    for i in range(len(b)):
        c += a[b[i]] * 8**(len(b)-i-1)
    print(c) 