def classificador(a,b,c):
    triangulo = a+b>c and a+c>b and b+c>a
    isosceles = a==b or a==c or b==c
    escaleno = a!=b and b!=c and c!=a
    equilatero = a==b==c
    retangulo = (a+b)==(c**2) or (a+c)==(b**2) or (b+c)==(a**2) 
    if triangulo: 
        print('triangulo')
    if triangulo and escaleno:
        print('escaleno')
    if triangulo and isosceles:
        print('isosceles')
    if triangulo and equilatero:
        print('equilatero')   
    if triangulo and retangulo:
        print('retangulo')
    if not triangulo:
        print('gondim sendo gondim')