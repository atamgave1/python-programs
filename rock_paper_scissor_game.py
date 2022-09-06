import random

print("Winning Rules of the Rock paper scissor game as follows: \n"+
"Rock vs paper->paper wins \n" +"Rock vs scissor->Rock wins \n"+"paper vs scissor->scissor wins \n")
while True:
    print("Enter Choice \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissor \n")
    choice = int(input("User Turn: \t"))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid Input:"))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    
    print("User Choice is:"+choice_name)
    print("\nNow it's Computer turn...: ")
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer choice is: " + comp_choice_name)
 
    print(choice_name + " V/s " + comp_choice_name)
    result = ''
    if comp_choice_name == choice_name:
         print("\nDraw=> ", end = "")
         result = "Draw"
    if((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )):
        print("\npaper wins => ", end = "")
        result = "paper"
 
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("\nRock wins =>", end = "")
        result = "Rock"
    else:
        print("\nscissor wins =>", end = "")
        result = "scissor"
 
    if result == "Draw":
        print("\n<== Its a tie ==>")
    elif result == choice_name:
        print("\n<== User wins ==>")
    elif result == comp_choice_name:
        print("\n<== Computer wins ==>")
         
    print("\nDo you want to play again? (Y/N)")
    ans = input().lower
  
    if ans == "n":
        break
     
print("\nThanks for playing")


