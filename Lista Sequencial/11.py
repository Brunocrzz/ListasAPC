def maiorAB (a,b):
    if a > b:
        print(a)
    else:
        print(b)
for i in range(5):
    a,b = input().split();a=int(a);b=int(b)
    maiorAB(a,b)    