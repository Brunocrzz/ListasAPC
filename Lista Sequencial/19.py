def quantosSemestres(m,a,s):    
  m = str(m);an = m[:2];sem = m[3:4];
  an = int(an);sem = int(sem);a = int(a);s = int(s)         
  anos = a - (an+2000)  
  calculo = (anos*2) + s  
  if sem and s == 1:
    calculo = (anos*2)+s-1
  if sem == 1 and s == 0:
    calculo = (anos*2)-1
  print(calculo)