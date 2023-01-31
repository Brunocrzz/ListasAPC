#Questão 16 ok

n = int(input())
def conta(n): 
    x = 0
    for i in range(n):
        a = int(input())
        b = 1000-a
        if a<1000:
            x+=b
        else:
            x+=0
    return x
print(conta(n))  