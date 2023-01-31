#Questão 39  ok

p = input()
x = 0
t = 0
while x<len(p)-1:
  if p[x]=='.' and p[x+1]=='o':
      t+=1
  x+=1
if p[0]=='o':
  print(t+1)
else:    
  print(t)