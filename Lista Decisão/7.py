def realidade(a,b,c):
    a=int(a);b=int(b);c = int(c)
    delta = (b**2) - (4*a*c)
    if delta >= 0:
        print('reais')
    else:
        print('complexas')