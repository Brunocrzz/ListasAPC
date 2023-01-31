#Questão 30 ok

n = int(input())
lista = []
if n==1:
  x = int(input())
  print(f'Menor: {x}')  
  print(f'Maior: {x}')
else:
  for i in range(n):
    x = int(input())
    lista.append(x)
  print(f'Menor: {min(lista)}')  
  print(f'Maior: {max(lista)}')