a = 20
if a >= 0:
    print (a);
else:
    print (-a); 
    

# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight/(height**2)
if bmi<=18.5:
    print("weighting too little")
elif bmi<=25:
    print("normal weight")
elif bmi<=28:
    print("little heavy")
elif bmi<=32:
    print("fat")
else:
    print("too fat")