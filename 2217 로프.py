r=[];ans=[];n=int(input())
for _ in range(n):
    r.append(int(input()))
r.sort(reverse=True)
for i in range(n):
    ans.append(r[i]*i+1)
print(max(ans))

