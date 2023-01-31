def maravilhosos(x):
    while x!=1:
        if x%2!=0:
            print(int(x))
            x = 3*x+1
        if x%2==0:
            print(int(x)) 
            x = x/2 
    print('1')        
x = int(input())
maravilhosos(x)             