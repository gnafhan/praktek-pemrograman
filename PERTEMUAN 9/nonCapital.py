def nonCapital(x:str):
    x= x.lower()
    x = list(x)
    x[0] = x[0].capitalize()
    x="".join(x)
    print(x)

nonCapital("CEk SaYa NaM")