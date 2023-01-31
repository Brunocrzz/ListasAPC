#Questão 33 ok
x = input()
a = list(x.split())
lista = (a[0:len(a)-1])
s = 1
final = []
for i in range(len(lista)):
  y = (lista[len(lista)-s])
  final.append(y)
  s+=1
print(*final)  
print(lista)