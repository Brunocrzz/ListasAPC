def pacotesDeBolacha(m,n,k): #M pacotes; N alunos; K - conseguem comer
    for i in range(k):
        if m >= n:
            m-=n
    print(m)        