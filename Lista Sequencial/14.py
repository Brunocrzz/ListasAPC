def age(i):
    A = int(i)//360
    M = (int(i)%360)//30
    D = int(i)-(A*360)-(M*30)
    print(f'{A} {M} {D}')
    
a,b,c = input().split()
age(a)
age(b)
age(c)