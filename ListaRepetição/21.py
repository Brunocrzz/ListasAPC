#Questão 21 ok

n = int(input())
for i in range(1,n+1):
    if i==1:
        print(i)
    elif i%3==0 and i%5==0:
        print('Fizz Buzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)   