
# Concanating two strings

greeting="Good Morning ,"
name="Aryadeep"
# print(type(name))
# print(greeting+name) 
c= greeting+name
print(c)

#Slicing
name="Aryadeep"
print(name[0])
print(name[1])
print(name[2])
# name[2]="d" --> does not work
print(name[0:3]) #0:3 means will print 0,1,2(0-2)
print(name[2:7]) #2:7 means will print 2,3,4,5,6(2-6)
print(name[:7]) #automatically detects as 0:7
print(name[0:]) #print all the string
print(name[2:]) #print all the string from 2:(length of the string)
print(name[-1])
print(name[-4])
print(name[-7])

arya="Aryadeep"
print(arya[1:8:1]) #takes range from 1:8(ryadeep)
print(arya[1::2]) #print 1:last with 1char diff
print(arya[0::3]) #print 0:last with 2char diff