#Questão 8 ok

senha = input()
if (
    6 <= len(senha) <= 32
    and any(x.isupper() for x in senha) #Se tem alguma letra maiuscula
    and any(x.islower() for x in senha) #Se tem alguma letra minuscula
    and any(x.isdigit() for x in senha) #Se tem algum numero
    and all(x.isalnum() for x in senha) #Se TODOS são alfanumericos
):    
    print('Senha valida.')
else:
    print('Senha invalida.')