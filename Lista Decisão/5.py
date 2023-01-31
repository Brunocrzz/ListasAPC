def dinheiros(n,a,b):
    if b*(n//2)<n*a:
        if n%2!=0:
            print(b*(n//2)+a)
        else:
            print(b*(n//2))
    else:
        print(n*a)