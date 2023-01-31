#Questão 7 ok 

Dolar = float(input())
Tamanho = int(input())
n = int(input())
conta = ((Dolar*0.025)+Dolar)*Tamanho
i=0
for i in range(n):
  i+=1
  print(f'Lote: {i} - Total da venda: R$ {conta:.2f}')