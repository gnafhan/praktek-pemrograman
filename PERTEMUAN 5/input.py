x = input("masukkan angka: ")
y= input("masukkan angka: ")

hasil = 0
for i in range(2):
    hasil += int(x.split()[i])
    hasil += int(y.split()[i])
print(hasil)