t = int(input())
for _ in range(t):
    t2 = int(input())
    max, a = 0, ""
    for _ in range(t2):
        name, num = input().split(); num = int(num)
        if num > max:
            max = num
            a = name
    print(a)