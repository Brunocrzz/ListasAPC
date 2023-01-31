#Questão 9 ok

n = int(input())
x = 0
b = '++X'
c = 'X++'
d = '--X'
e = 'X--'
def conta(n):
    x = 0    
    for i in range(n):
        a = input()
        if a==b or a==c:
          x+=1
        elif a==d or a==e:
         x-=1
    return x    
print(conta(n))  