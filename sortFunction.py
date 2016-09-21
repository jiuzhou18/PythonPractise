L=[('bob', 23), ('jame', 28), ('kitty', 19), ('bill', 32)]
def byName(t):
    return t[0].lower()


SL = sorted(L, key=byName)
print(SL)

SL2 = sorted(L, key = (lambda x: x[1]))
print(SL2)

