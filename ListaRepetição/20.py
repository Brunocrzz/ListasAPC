#Questão 20 ok

def fibonacci(n):
    lista = []
    for i in range(n):
      if i<2:
        lista.append(i)
      else:
        lista.append(lista[len(lista)-2] + lista[len(lista)-1]) 
    print(*lista)  
