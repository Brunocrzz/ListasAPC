def piscininha(x,y,w,h,a,b):
    x=int(x);y=int(y);w=int(w);h=int(h);a=int(a);b=int(b)
    borda=x+w
    borda1=y+h
    if a==x or b==y:
        print('So com os pezin dentro da agua')
    elif a>x and a<borda and b>y and b<borda1:
        print('Dando um tchibum')
    else:
        print('Tomando um solzin')