#password generator
import string
import random
#taking size as input
size=int(input("Enter the size of password: "))
print('''choose the option which you want to include in your password:
      1.Numbers
      2.aplphabets
      3.special character
      4.exit''')

characterlist=" "
while(True):
    choice=int(input("Pick a number: "))
    if (choice==1):
      #adding digit to possible character
      characterlist+=string.digits
    elif choice==2:
      
       #adding alphabets to possible character
       characterlist+=string.ascii_letters
    elif choice==3:
     
       characterlist+=string.punctuation
    elif choice==4:
       break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(size):
   
    # Picking a random character from our 
    # character list
    randomchar = random.choice(characterlist)
     
    # appending a random character to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))
       

       
