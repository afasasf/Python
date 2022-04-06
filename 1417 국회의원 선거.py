t = int(input())
d = int(input())
if t <= 1:
    print(0)
else:
    vote = []
    for _ in range(t-1):
        vote.append(int(input()))
    
    result = 0
    while max(vote) >= d:
        b = vote.index(max(vote))
        d += 1
        vote[b] -= 1
        result += 1
    print(result)