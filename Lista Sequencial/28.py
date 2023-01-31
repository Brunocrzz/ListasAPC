def print_rectangle(a):
    print(a);print('x'*a);print("x", "x",  sep=' '*(a-2), end="\n");print("x", "x",  sep=' '*(a-2), end="\n");print('x'*a)
a = input().split(); 
for i in (a):
    print_rectangle(int(i))