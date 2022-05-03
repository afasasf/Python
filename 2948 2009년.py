m=[31,28,31,30,31,30,31,31,30,31,30,31]
d=['Wednesday','Thursday','Friday','Saturday','Sunday','Monday','Tuesday']
D,M=map(int,input().split())
print(d[(sum(m[:M-1])+D)%7])