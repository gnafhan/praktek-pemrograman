def singkatan(x):
    hasil = []
    for i in range(len(x)):
        if str(x[i]).isupper():
            hasil.append(x[i])
    return " ".join(hasil)

def gambar(huruf):
    for i in range(len(huruf)):
        
        if huruf[i] == "A":
            print("   __   ")
            print("  / _\  ")
            print(" /    \ ")
            print("/__/\__\\")
        elif huruf[i] == "B":
            print("  ___  ")
            print(" | _ ) ")
            print(" | _ \ ")
            print(" |___/ ")
        elif huruf[i] == "C":
            print("   ___ ")
            print("  / __|")
            print(" | (__ ")
            print("  \___|")
        elif huruf[i] == "D":
            print("  ___  ")
            print(" |   \ ")
            print(" | |) |")
            print(" |___/ ")
        elif huruf[i] == "E":
            print("  ___ ")
            print(" | __|")
            print(" | _| ")
            print(" |___|")
        elif huruf[i] == "F":
            print("  ___ ")
            print(" | __|")
            print(" | _| ")
            print(" |_|  ")
        elif huruf[i] == "G":
            print("  ___  ")
            print(" / __| ")
            print(" \__ \ ")
            print(" |___/ ")
        elif huruf[i] == "H":
            print("  _  _  ")
            print(" | || | ")
            print(" | __ | ")
            print(" |_||_| ")
        elif huruf[i] == "I":
            print("  _  ")
            print(" (_| ")
            print(" | | ")
            print(" |_| ")
        elif huruf[i] == "J":
            print("    _  ")
            print("   (_| ")
            print("   | | ")
            print("  _/ | ")
            print(" |__/  ")
        elif huruf[i] == "K":
            print("  _  __")
            print(" | |/ /")
            print(" | ' < ")
            print(" |_|\_\\")
        elif huruf[i] == "L":
            print("  _    ")
            print(" | |   ")
            print(" | |__ ")
            print(" |____|")
        elif huruf[i] == "M":
            print(" __  __ ")
            print(" |  \/  |")
            print(" | |\/| |")
            print(" |_|  |_|")
        elif huruf[i] == "N":
            print("  _  _ ")
            print(" | \| |")
            print(" | .` |")
            print(" |_|\_|")
        elif huruf[i] == "O":
            print("  ___  ")
            print(" / _ \ ")
            print("| (_) |")
            print(" \___/ ")
        elif huruf[i] == "P":
            print("  ___  ")
            print(" | _ \ ")
            print(" |  _/ ")
            print(" |_|   ")
        elif huruf[i] == "Q":
            print("  ___  ")
            print(" / _ \ ")
            print("| (_) |")
            print(" \__\_\\")
        elif huruf[i] == "R":
            print("  ___  ")
            print(" | _ \ ")
            print(" |  _/ ")
            print(" |_|   ")
        elif huruf[i] == "S":
            print("  ___  ")
            print(" / __| ")
            print(" \__ \ ")
            print(" |___/ ")
        elif huruf[i] == "T":
            print("  ___  ")
            print(" |_ _| ")
            print("  | |  ")
            print("  |_|  ")
        elif huruf[i] == "U":
            print("  _  _  ")
            print(" | || | ")
            print(" | || | ")
            print(" |____| ")
        elif huruf[i] == "V":
            print(" __   __")
            print(" \ \ / /")
            print("  \ V / ")
            print("   \_/  ")
        elif huruf[i] == "W":
            print(" __     __")
            print(" \ \   / /")
            print("  \ \ / / ")
            print("   \ V /  ")
            print("    \_/   ")
        elif huruf[i] == "X":
            print(" __  __")
            print(" \ \/ /")
            print("  >  < ")
            print(" /_/\_\\")
        elif huruf[i] == "Y":
            print(" __   __")
            print(" \ \ / /")
            print("  \ V / ")
            print("   |_|  ")
        elif huruf[i] == "Z":
            print("  ____")
            print(" |_  /")
            print("  / / ")
            print(" /___|")
        else:
            print("")

gambar(singkatan("Dinar Nugroho Pratomo"))
