#CBadley
#Sept 2021
#Ask for number and calculate times tables

#ask for the number

num_one = (input ("\nPLease give me a whole number between 1 and 12\n"))

while num_one.isdigit()==False or int(num_one)>= 13:

    print ("\nThat's not a whole number between 1 and 12!")
    num_one = (input ("\nPLease give me a number between 1 and 12\n"))

print ("I'm now going to print the",num_one,"times table. Are you ready?!")

i = 1
while i < 13:
    print (i, "x", num_one,"=", i*int(num_one))
    i = i+1



