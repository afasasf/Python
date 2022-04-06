a, b, v = map(int, input().split())
c = 0
d = 0

for _ in range(1):
    c+=1
    if c>=(v-b)/(a-b):
        break
print(c)