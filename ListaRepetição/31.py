#Questão 31 ok

n = int(input())
i = 2 

print('1 elefante incomoda muita gente...')
print('2 elefantes incomodam, incomodam muito mais...')

while i<=n:
    print(f'{i} elefantes incomodam muita gente...')
    print(f'{i+1} elefantes {"incomodam, "*(i)}incomodam muito mais...')
    
    i+=1