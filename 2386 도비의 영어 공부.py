while (a:=input()) != '#':
    print(a[0], a[2:].lower().count(a[0]))