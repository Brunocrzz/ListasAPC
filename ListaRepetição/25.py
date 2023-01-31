#Questão 25 ok
def ppa(a,b):
    pedra = 1
    papel = 2
    aereo = 3
    if a==3 and b==1 or b==3 and a==1:
        if a>b:
            return('Jogador 1 venceu')
        else:
            return('Jogador 2 venceu')
    elif a==2 and b==1 or b==2 and a==1:   
        if a>b:
            return('Jogador 2 venceu')
        else:
            return('Jogador 1 venceu')
    elif a==2 and b==3 or b==2 and a==3:   
        if a>b:
            return('Jogador 1 venceu')
        else:
            return('Jogador 2 venceu') 
    elif a==2 and b==2:
        return ('Ambos venceram')
    elif a==1 and b==1: 
        return ('Sem ganhador')
    elif a==3 and b==3:
        return('Aniquilacao mutua')