a = [*map(int, input().split(':'))]
b = [*map(int, input().split(':'))]

h = b[0] - a[0]
m = b[1] - a[1]
s = b[2] - a[2]

if s < 0:
    s += 60
    m -= 1
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24

print('%02d:%02d:%02d' %(int(h),int(m),int(s)))