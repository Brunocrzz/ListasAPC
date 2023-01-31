def pacotesDeBolacha(m,n,k): #M pacotes; N alunos; K - conseguem comer
    l = 0
    for i in range(k):
        if m >= n:
            m-=n
            l += n
    print(l)        