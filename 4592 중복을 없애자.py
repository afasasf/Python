while True:
    _, a=input(), ''
    if _ == '0':
        break
    for i in _.split()[1:]:
        if i == a: 
            continue
        print(i, end=' ')
        a = i
    print('$')
