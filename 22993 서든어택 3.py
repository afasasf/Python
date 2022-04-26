n = int(input())
a_list = [*map(int, input().split())]
a = a_list[0]
aa = True
a_list = sorted(a_list[1:])
for i in a_list:
    if a > i:
        a += i
    else:
        aa = False
        break
print('Yes' if aa else 'No')