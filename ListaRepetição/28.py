#Questão 28 ok

a = list(map(int,input().split()))
print(f'{min(a)} {a.index(min(a))}')
print(f'{max(a)} {a.index(max(a))}')
for i in range(len(a)):
    print(a[i], end=' ')