def print_rectangle(a):
    print(a);print('+'*a);print("+", "+",  sep=' '*(a-2), end="\n");print('+'*a)
a = input().split(); 
for i in (a):
    print_rectangle(int(i))