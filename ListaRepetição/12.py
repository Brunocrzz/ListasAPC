#Questão 12 ok

n = int(input())
lista = list(map(int, input().split()))
maior = int(max(lista))
fim = []
x = 0
for i in range(n):
  a = int(lista[x])
  b = maior-a
  fim.append(b)
  x+=1
for i in range(len(lista)):
    print(max(lista) - lista[i], end=' ')