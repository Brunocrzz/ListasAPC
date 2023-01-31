num = input()
x,y,z = num.split()
x = float(x);y = float(y);z = float(z)

c1 = x+(x/10); 
c2 = y+(y/10)
c3 = z+(z/10)
total = c1+c2+c3

def f():
  f = '%.2f'%float(c1)
  return f

def t():
  j = '%.2f'%float(c2)
  return j

def j():
  j = '%.2f'%float(c3)
  return j

  
print(f'{f()} {t()} {j()}')
print('%.2f'%float(total))