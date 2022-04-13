a = [list(map(int, input().split())) for _ in range(3)]
for i in a:
    if sum(i) == 3:
        print('A')
    elif sum(i) == 2:
        print('B')
    elif sum(i) == 1:
        print('C')
    elif not sum(i):
        print('D')
    elif sum(i) == 4:
        print('E')