#Questão 13 ok

x = int(input())
lista = [x]
while x!=-1:
  x = int(input())
  lista.append(x)
y = sum(lista)+1
z = len(lista)-1
print(y//z)
