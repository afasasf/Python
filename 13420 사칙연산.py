for _ in[0]*int(input()):
    a, b=map(str, input().split('='))
    print("correct") if eval(a)==int(b) else print("wrong answer")