t = int(input())

for _ in range(t):
    s = input().lower()

    if s == s[::-1]:
        print("Yes")
    else:
        print("No")