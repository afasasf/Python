a = list(input())
b = 0

if a[0] == " ":
    b += 1
if a[len(a)-1] == " ":
    b += 1

print(a.count(" ") - b + 1)