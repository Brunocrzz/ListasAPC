#Questão 35 ok

a = list(input())
b = []
x = 1
if a[0]=='-':
  b.append(a[0])
  while x!=len(a):
    b.append(a[len(a)-x])
    x+=1
  b = ''.join(map(str,b))  
  print(int(b))
else:    
  while x!=len(a)+1:
    b.append(a[len(a)-x])
    x+=1
  b = ''.join(map(str,b))
  print(int(b))