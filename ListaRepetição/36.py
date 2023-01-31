#Questão 36 OK

def remove_duplicatas(x):
  lista = []
  for i in x: 
    if i not in lista:
      lista.append(i)
  return lista       