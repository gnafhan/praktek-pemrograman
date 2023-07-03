def halaman(x:int):
    for i in range(x):
        x-=1
        if x <= 0:
            print("senin")
            break
        x -= 1
        if x <= 0:
            print("selasa")
            break
        x -= 1
        if x <= 0:
            print("rabu")
            break
        x -= 1
        if x <= 0:
            print("kamis")
            break
        x -= 2
        if x <= 0:
            print("jumat")
            break
        x -= 1
        if x <= 0:
            print("sabtu")
            break
        x -= 3
        if x <= 0:
            print("minggu")
            break

halaman(7)