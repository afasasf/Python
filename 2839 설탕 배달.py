a = int(input())
b = a // 5
c = a % 5
ab = [4, 7]
if a in ab:
    bag=-1
elif c==1 or c==3:
    bag=b+1
elif c==2 or c==4:
    bag=b+2
else:
    bag=b
print(bag)