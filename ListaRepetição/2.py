#Questão 2 ok

def soma_harmonica(X):
    if X==1:
        return (1)
    elif X>0:
        k=0
        soma = 0
        for i in range (X):
            k+=1
            soma+=1/k
        return (soma)    