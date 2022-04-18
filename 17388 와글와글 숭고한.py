s = [*map(int, input().split())]
if sum(s) >= 100: print('OK')
elif min(s) == s[0]: print('Soongsil')
elif min(s) == s[1]: print('Korea')
else: print('Hanyang')