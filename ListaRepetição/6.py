#Questão 6 ok

n = int(input())
b = input()
lista = list(b.split())
lista[:] = list(map(int,lista))
lista2 = []
for i in range(n):
  lista2.append((lista[i]-min(lista)))
print(*lista2)  