L = [1,3,4,7,9,0,12,34,56,123]

def addision(x):
    for i in range(len(L)):
        L[i] += x

addision(3)
print(L)