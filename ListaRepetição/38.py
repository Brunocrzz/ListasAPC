#Questão 38 OK

n = int(input())
for i in range(n):
  x = 0
  l = 0
  p = input()
  if p[0]=='0':
      x+=1
  while x<len(p)-1:
    if p[x]=='1' and p[x+1]=='0' and '1' in p[x+1:len(p)]:
      l+=1
    elif '1' in p[0:x] and p[x]=='0' and p[x+1]=='1' and p[x-1]!='1':
      l+=1
    elif '1' in p[0:x] and p[x-1]=='0' and p[x]=='0' and p[x+1]=='0' and '1' in p[x+1:len(p)]:
      l+=1    
    x+=1  
  print(l)    