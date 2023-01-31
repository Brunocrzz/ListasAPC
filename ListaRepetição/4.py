#Questão 4 ok 

def media(N):
    y = 0
    for i in range(N):
        a = input()
        as1,as2,as3=a.split()
        as1 = float(as1)
        as2 = float(as2)
        as3 = float(as3)
        if (as1+as2+as3)/3>=7:
            print(f'O ALUNO {y} FOI APROVADO')
        else:
            print(f'O ALUNO {y} FOI REPROVADO')
        y+=1
        

N = int(input())
media(N)