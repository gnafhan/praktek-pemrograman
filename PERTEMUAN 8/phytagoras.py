def phytagoras(x:int):
    for i in range(x):
        for j in range(x):
            if i*i + j*j == x*x:
                print(i, j)

phytagoras(25)