#Questão 24 ok

k = int(input());l = int(input());m = int(input());n = int(input());d = int(input())
t=0
x=0
for i in range(d):
    if k==1:
      t=k
    elif x%k==0 or x%l==0 or x%m==0 or x&n==0: 
        t+=1
    x+=1   
   
print(t)  