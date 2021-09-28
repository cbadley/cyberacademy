#CBadley
#Sept 2021
#password checker
import re

password_input = input("Please enter a 10 charactor password. It can contain upper case, lower case or numbers. I will tell you if you password is weak, medium or strong.\n")

#checking the length of the password
while len(password_input)!=10:
    print ("\nThat's not a password with 10 characters!")
    password_input = input ("\nPlease enter a 10 charactor password.\n")

#asking for password to be entered again
password_check = input("Please re-enter you password")

#checking the two passwords match
while password_check != password_input:
    print ("\nYour passwords do not match")
    password_input = input ("\nPlease enter a 10 charactor password.\n")
    password_check = input("Please re-enter your password")


#checking whether capital letters, lowercase letters or numbers exist in the variable password_input
capital_match = re.search(r"[A-Z]", password_input)
lower_match = re.search(r"[a-z]", password_input)
digital_match = re.search(r"[0-9]", password_input)


#where the password has lowercase, uppercase and numerals
if capital_match and lower_match and digital_match:
    print("You have created a strong password")
    
#all numbers
elif not capital_match and not lower_match:
    print("You have created a weak password")
    
#all capitals
elif not lower_match and not digital_match:
     print("You have created a weak password")
     
#all lowercase
elif not capital_match and not digital_match:
     print("You have created a weak password")
     
#every other combination wil be medium strength
else:
    print ("Your password is medium strength")
    
