def floor(x:float):
    if x%1 >= 0.4:
        return int(x)+1
    else:
        return int(x)//1
    
# print(floor(float(input())))

def middle(x,y,z):
    if x>y and z>x:
        return x
    elif y>x and z>y:
        return y
    else:
        return z
    
# print(middle(9,1,6))

def dateIsValid(x,y,z):
    isKabisat = False
    if z%4 == 0:
        isKabisat = True
    if y == 2:
        if x > 28:
            if isKabisat and x == 29:
                print('valid')
            else:
                print('tidak valid')
        else:
            print('valid')
    if x>30 and y!=2:
        if x>31:
            print('tidak valid')
        elif y == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            print('valid')
        else:
            print('tidak valid')

    elif y!=2: 
        print("valid")
dateIsValid(32, 3, 2000)
