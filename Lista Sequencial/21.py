nota = input()
n1,n2,n3 = nota.split(); n1=float(n1);n3=float(n3);n2=float(n2)
peso = input()
p1,p2,p3 = peso.split(); p1=int(p1);p3=int(p3);p2=int(p2)

N1 = n1*p1;N2 = n2*p2;N3 = n3*p3
T = N1+N2+N3
S = p1+p2+p3
Média = T/S

print(f'{Média:.6f}')