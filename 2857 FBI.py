res=[]
for i in range(1, 6):
    if 'FBI' in input():
        res.append(str(i))
print(' '.join(res) if res else "HE GOT AWAY!")