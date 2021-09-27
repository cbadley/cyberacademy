#CarolineBadley
#Sept2021
#random guess limited number of goes
import random #imports random library

print ("\n\tHello and welcome to the Guess Your Number Game \n\n")

myName = input ("Hello! What is your name? ")
number = random.randint(1,10) #random generation between 1 and 10

print ("Well,  " + myName + " I am thinking of a number between 1 and 10.")

guess = int(input("\nTake a guess at what number I'm thinking of:") )

#analyse if the number correct
if guess == number:
    print ("Well done you've guessed it")

#if the number is not correct  
else:
    turns = 0
    while turns < 2:
        print ("Sorry that's not right")
        #if the number they have guessed is too low
        if guess<number:
            print ("Your guess was too low")
        #if the number they have guessed is too high
        else:
            print ("Your guess was too high")

        #find out whether the user wants another go    
        again = input("\nWould you like to take another guess: yes/no\n")
        if again =="yes":
            guess = int(input("\nTake another guess:") )
            if guess == number:
                print ("Well done you've guessed it")
                break                                            
        else:
            print ("Well be like that then! See ya!")
            #stop the code here as they don't want to play anymore
            break
        
        #go back to while
        turns = turns +1
        
    if turns >=2:
        print ("Sorry you're out of turns")

    

            

           
    
    


            



    
