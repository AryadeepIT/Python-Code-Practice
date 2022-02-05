n=3
col=3
for i in range(3):
    for j in range(3):
        if i==0 or i==2 or i+j==1 or i+j==3:
            print("*",end="")
        else:
            print(" ",end="")
            print()