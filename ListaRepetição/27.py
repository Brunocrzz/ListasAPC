#Questão 27 ok

def ehPrimo(x):
  y = 0 
  for i in range(1,x):
    if x%i==0:
      y+=1
  if y>1:
    return 0
  else:
    return 1         
def divisoresPrimos(x):
  y = 0
  for i in range(2,x):
    if ehPrimo(i)==1:    
      if x%i==0:
         y+=1
  return y 
