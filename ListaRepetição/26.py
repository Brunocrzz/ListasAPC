#Questão 26 ok
n = int(input())
t = 0
for i in range(n):
    s = input()
    a,b,c = s.split()
    a = int(a);b=int(b);c=int(c)
    t += a+b+c
    
if t==0:
    print('YES')
else:
    print('NO')