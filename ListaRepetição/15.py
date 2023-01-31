#Questão 15 ok

dados = input()
a,b,c,d = dados.split()
a = int(a);b = int(b); c = float(c);d = float(d)
Pa = (c/100)
Pb = (d/100)
Ca = int(a+(Pa*a))
Cb = int(b+(Pb*b))
x = 1
if b > a and d > c:
  print('A nunca alcancara B.')
else:
  while Cb>Ca:
    Ca = int(Ca+(Pa*Ca))
    Cb = int(Cb+(Pb*Cb)) 
    x+=1 
  if x>1000:
    print("Mais de um milenio.")
  else:
    print(f"Vai alcancar em {x} ano(s).")   