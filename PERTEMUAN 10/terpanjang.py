def terpanjang (x:list):
    panjang = 0
    nama = ""
    for i in range(len(x)):
        if len(x[i]) > panjang:
            panjang = len(x[i])
            nama = x[i]
    return nama

a = ["Asep", "Nurhadi", "Joko", "Doni", "Andi", "Sutrisnowati"]
print(terpanjang(a))