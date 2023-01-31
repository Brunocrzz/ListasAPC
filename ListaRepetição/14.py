#Questão 14 ok

def MDC(a, b):
  while(b != 0):
    resto = a % b 
    a = b
    b = resto    
  return a
n = input()  
a,b = n.split()
a= int(a);b=int(b)
if MDC(a,b)==1:
  print('Sao co-primos.')
else:
  print('Nao sao co-primos!')  