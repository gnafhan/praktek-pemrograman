import math
def SumThreeDigitsNumber(x):
    hasil = 0
    y= x%10
    hasil = hasil + y
    y = x/10
    y = math.floor(y)
    z = y%10
    hasil = hasil + z
    return hasil + math.floor(y/10)

print(SumThreeDigitsNumber(999))

#maaf anak js


def AnakPython(x):
    hasil = x//100
    y = x%100
    return hasil + y//10 + y%10

print(AnakPython(888))
