def add_end(L=[]):
    L.append('#')
    return L

add_end()
add_end()
print("This is trick L :", add_end())


def add_end_stay(L=None):
    if L is None:
        L=[];
    L.append('end')
    return L

add_end_stay()
add_end_stay()
print("This L will be renew evertime:", add_end_stay())
        
        
def change (*numbers):
    for num in numbers:
        num = num+1;
        print (num, end=" ")
numbers1 = [1,2,3]
change(*numbers1)
print("\n",numbers1,end="")

