def banner(n):
    n = int(n)
    if n%2==0 and n>0:
        print("| | | | | | | | | | ")
    elif n%2==1 and n>0:
        print("- - - - - - - - - -")
    elif n%2==0 and n<0:
        print(". . . . . . . . . .")
    elif n%2==1 and n<0:
        print("= = = = = = = = = =") 
