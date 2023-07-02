kapital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def isKapital(x:str):
    juml = 0
    for i in range(len(x)):
        if x[i] in kapital:
            juml+=1

    return juml
print(isKapital("CEk"))