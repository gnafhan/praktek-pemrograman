def keliling(x):
    for i in range(x):
        if i in [0,x-1] :
            print("#"*x)
        else:
            print("#"," "*(x-4),"#")
keliling(16)