def quantosJantam(n,g,f,c):
    t = min(g,f)
    total = t+c
    if n==0:
        print(0)
    elif n<total:
        print(n)
    else:
        print(total) 