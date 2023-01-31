seg = input()
A,Y,Z = seg.split(':')
A = int(A);Y = int(Y); Z = int(Z)

def conta():
  S = Z; S = int(S)
  F = Y*60; F = int(F)
  G = 3600*A ; G = int(G)
  Total = S+F+G
  return Total 

X = (conta())

print("La se foram" , X ,"segundos que nao voltam mais...") 
