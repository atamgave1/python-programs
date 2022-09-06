import random
import math

lower = int(input("Enter Lower bound\t"))
upper = int(input("Enter Upper bound\t"))
x=random.randint(lower,upper)
print (f"you have only {round(math.log(upper-lower+1,2))} chances to guess the integer\n")

count = 0
while count < math.log(upper-lower+1,2):
    count+=1

    guess= int(input("Guess the Number:\t"))
    if x== guess :
        print(f"Congratulations! You did it in {count} try\n")
        break
    elif(guess > x):
        print("Try Again! You guessed to High\n")
    elif(guess < x):
        print("Try Again! You guessed to small\n")

if( count>= math.log(upper-lower-1,2)):
    print("The Number is %d\n"%x)
    print("Better luck next time\n")
