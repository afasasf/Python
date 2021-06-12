a = int(input())

if a % 2 != 0:
    b = a//2
    print('*'*a)
    print(' '*(a-b-1) + '*')
    for i in range(b):
        print(' '*(b-i-1) + '*' + ' '*(2*i+1) + '*')
else:
    print("I LOVE CBNU")