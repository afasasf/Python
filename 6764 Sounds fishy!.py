a = [int(input()) for _ in range(4)]
cnt=0
for i in range(3):
    if a[i+1] > a[i]: 
        cnt += 1
    elif a[i+1] < a[i]:
        cnt -= 1

if len(set(a)) == 1:
    print('Fish At Constant Depth')
elif cnt == 3:
    print('Fish Rising')
elif cnt == -3:
    print('Fish Diving')
else:
    print('No Fish')