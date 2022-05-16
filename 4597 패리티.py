while 1:
    a=input()
    if a=='#': break
    else:
        cnt=a.count('1')
        if a[-1]=='e':
            if cnt%2==1: a=a[:-1]+'1'
            else: a=a[:-1]+'0'
        else:
            if cnt%2==1: a=a[:-1]+'0'
            else: a=a[:-1]+'1'
        print(a)
