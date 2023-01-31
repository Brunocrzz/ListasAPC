#Questão 19 ok

def fibonacci(n):
    lista = []   
    if n==0:
      return 0
    for i in range(n+1):
      if i<2:
        lista.append(i)
      else:
        lista.append(lista[len(lista)-2] + lista[len(lista)-1]) 
    return (lista[n]) 
  