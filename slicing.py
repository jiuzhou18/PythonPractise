L=['Mick', 'Jack', 'Jame', 'Simon', 'Mary']
H = L[-2:]
print(H)
L[-1] = 'New'
print(H)
H[1] = 'Renew'
print(L)
print(L[::2])


d = {'a':1, 'b':2, 'c':3}
for k,v in d.items():
    print ("the key", k,"with value", v )
    
S = "This is a new string"
print(S[:7])

for ch in S[-4:-1]:
    print ("The letters in S is:", ch)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
