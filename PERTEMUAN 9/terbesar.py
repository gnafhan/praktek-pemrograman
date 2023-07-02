def highest (x, y, z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

print(highest(3,1,1))