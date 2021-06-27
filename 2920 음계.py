a = list(map(int, input().split()))

if a == sorted(a):
    print("ascending")
elif a == sorted(a, reverse=True):
    print("descending")
elif a != a.sort() or a != a.sort(reverse=True):
    print("mixed")