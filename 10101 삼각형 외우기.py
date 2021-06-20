a = int(input())
b = int(input())
c = int(input())
sum = a+b+c

if sum == 180:
    if a==b==c:
        print("Equilateral")
    elif a!=b==c or a==b!=c or a==c!=b:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")