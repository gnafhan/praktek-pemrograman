nama = ["budi", "alam", "nana", "ardi", "neil"]
for i in range(len(nama)):
    for j in range(len(nama)):
        if nama[i] < nama[j]:
            nama[i], nama[j] = nama[j], nama[i]

for i in range(len(nama)):
    print(nama[i])