a=''
while 1:
    try:
        a+=input()
    except EOFError:
        break
print(sum(map(int, a.split(','))))