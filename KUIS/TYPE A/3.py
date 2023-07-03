x = input()
y = input()
print("")
a=input()
b=input()
hasil = 0
kiriatas = 0
kananatas=0
kiribawah = 0
kananbawah = 0

for i in range(2):

    if i == 0:
        kiriatas = (int(x.split()[i])*int(a.split()[i])+int(x.split()[1])*int(b.split()[i]))
        kiribawah = (int(y.split()[i])*int(a.split()[i])+int(y.split()[1])*int(b.split()[i]))
    elif i == 1:
        kananatas = (int(x.split()[0])*int(a.split()[i])+int(x.split()[i])*int(b.split()[i]))
        kananbawah = (int(y.split()[0])*int(a.split()[i])+int(y.split()[i])*int(b.split()[i]))

print("")
print(str(kiriatas)+" "+str(kananatas))
print(str(kiribawah)+" "+str(kananbawah))