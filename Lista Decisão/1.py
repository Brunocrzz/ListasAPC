def area(x,y,z):
    x = int(x); y=int(y)
    if z == 'losango':
        a = x*y//2
        print(f'O {z} tem {a} de area')
    else:
        b = x*y
        print(f'O {z} tem {b} de area')