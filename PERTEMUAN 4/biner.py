def biner(x:str):
    hasil = 0
    for i in range(5):
        hasil = hasil + int(x[i])
    return hasil

print(biner("01111"))

def BinerPisah(x:str):
    hasil = 0
    for i in range(5):
        hasil = hasil + int(x.split()[i])
    return hasil

print(BinerPisah("1 1 1 1 1"))