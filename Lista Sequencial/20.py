def qualPeriodo(m,a,s):    
  m = str(m);an = m[:2];sem = m[3:4];
  an = int(an);sem = int(sem);a = int(a);s = int(s)         
  anos = a - (an+2000)   
  if sem == 0 and s == 0 :
    calculo = (anos*2)+1
  if sem == 0 and s == 1 :
    calculo = (anos*2)+2
  if sem == 1 and s == 1 :
    calculo = (anos*2)+1
  if sem == 1 and s == 0 :
   calculo = (anos*2)
  print(calculo)