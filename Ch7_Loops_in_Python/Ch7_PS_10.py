num=int(input("enter a number :"))
tablelist=[]
for i in range(1,11):
    tablelist.append(i*num)
    tablelist.reverse()
    print(tablelist)