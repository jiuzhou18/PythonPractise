def hanoi (n,a,b,c):
    if n==1:
        print("Move one plate No.", n, " form ", a, " to ", c, ".\n", end="")
    else:
        hanoi(n-1,a,c,b)
        print("Move one plate No.", n, " form ", a, " to ", c, ".\n", end="")
        hanoi(n-1,b,a,c)
        
n = input("please input a integer:")
hanoi(int(n),'A','B','C')
