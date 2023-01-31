#Questão 22 ok

def pattern(n):
    x = n
    while x>0:
        print(x)
        x-=5
    while x!=n:
        print(x)    
        x+=5
    print(n)    