def qtdcopos(n):
    if n%4!=0:
        print(f'Pode voltar pro ceubinho, deivis! Falta(m) {4-(n%4)} copo(s)!')
    if n==0:
        print('Pode voltar pro ceubinho, deivis! Falta(m) 4 copo(s)!')
    elif n%4==0:
        print("Pode levar pros calourinhos, deivis!")        