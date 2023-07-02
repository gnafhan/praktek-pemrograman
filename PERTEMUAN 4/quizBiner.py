def binerToDecimal(x:str):
    hasil = 0
    for i in range(4):
        if int(x[i]) == 1:
            hasil += (2**(3-i))
    return hasil        




print(binerToDecimal('1101'))