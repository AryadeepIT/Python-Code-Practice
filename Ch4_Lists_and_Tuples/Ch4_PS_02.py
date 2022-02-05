'''Q :- Write a program to accept the marks of 6 students and display them in a sorted manner.'''

m1=int(input("Enter Student number 1 marks in list  :"))
m2=int(input("Enter Student number 2 marks in list  :"))
m3=int(input("Enter Student number 3 marks in list  :"))
m4=int(input("Enter Student number 4 marks in list  :"))
m5=int(input("Enter Student number 5 marks in list  :"))
m6=int(input("Enter Student number 6 marks in list  :"))

mysortlist=[m1,m2,m3,m4,m5,m6]
mysortlist.sort()
print(mysortlist)