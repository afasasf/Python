#import sys
#n = int(sys.stdin.readline())
#a = []
#for _ in range(n):
#    b = int(sys.stdin.readline())
#    a.append(b)
#
#for i in sorted(a):
#    print(i)
import sys
input=sys.stdin.readline
a=[]
for i in " "*int(input()) :a+=int(input()),
print("\n".join(list(map(str,sorted(a)))))