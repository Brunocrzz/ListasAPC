#Questão 1 Ok
def anobissexto(a):
    if a%400!=0 and a%100==0:
        return 'Nao'
    elif a%4==0:
        return 'Sim'
    else:
        return 'Nao'
a = input('Qual valor de a?')    
a = int(a)   
print(anobissexto(a))