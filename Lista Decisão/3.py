def area(x,y,z):
    x = int(x); y=int(y)
    if z == 'losango':
        a = x*y//2
        print(f'O {z} tem {a} de area')
    elif z == 'retangulo':
        b = x*y
        print(f'O {z} tem {b} de area')
    elif z == 'triangulo':
        print(f'O {z} tem {(x*y)//2} de area')
    elif z == 'circulo':
        print(f'O {z} tem {(y*(x**2))} de area')