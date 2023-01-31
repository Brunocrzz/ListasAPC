#Questão 17 ok 

num = input()
a,b = num.split()
a = int(a);b = int(b)
lista = []
for i in range(a):
  x = int(input())
  lista.append(x)
c = sum(lista)
f = len(lista) 
print(f'media: {c//f}')
if c//f >= b:
  print('o rock reinara mais uma vez')
else:
  print('rockeiros trabalhando ja')  