#Questão 29 ok

n = int(input())
x = 0
for i in range(n):
  num = input()
  a,b,c = num.split(); a = int(a); b = int(b); c = int(c)
  if a==1 and b==0 and c==1 or a==0 and b==1 and c==1 or a==1 and b==1 and c==0:
    x+=1
  elif a==1 and b==1 and c==1:
    x+=1
print(x)