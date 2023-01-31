def formamisteriosa(a,b,c):
    triangulo = a+b>c and a+c>b and b+c>a
    isosceles = a==b or a==c or b==c
    escaleno = a!=b and b!=c and c!=a
    equilatero = a==b==c
    if a==b:
        print('pode ser quadrado')
    elif a>b or a<b:
        print('pode ser retangulo')
    if triangulo and escaleno:
        print('pode ser triangulo escaleno')
    elif triangulo and equilatero:
        print('pode ser triangulo equilatero')
    elif triangulo and isosceles:
        print('pode ser triangulo isosceles')    
    elif triangulo: 
        print('pode ser triangulo')