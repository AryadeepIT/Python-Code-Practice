'''Write a program to fill in a letter template given below with name and date.
        letter = '" Dear <|NAME|>,

                        You are selected!

                        <|DATE|>
'''

letter='''Dear <|NAME|>, 
You are selected!
         Date :   <| DATE |>
'''
name=input("Enter Your Name :")
date=input("Write today date :")
letter=letter.replace("<|NAME|>" , name)
letter=letter.replace("<| DATE |>" , date)
print(letter)