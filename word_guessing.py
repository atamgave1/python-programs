import random

name = input("What is your name?\t")
print("Good Luck! ",name)

words=['rain','cloud','soil','water','rainbow','ship','computer','python','Umbrella','science','mathematics',
        'football','ocean','player']

word = random.choice(words)
print("Guess the characters\n")
guesses = ''
turns = 12
while turns > 0 :
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end =" ")
        else:
            print("_")
            failed+=1
    if failed == 0 :
        print("You Win")
        print("The word is:",word)
        break
    print("Enter another alphabet\t")
    guess = input("Guess a character\t")

    guesses+=guess
    if guess not in word:
        turns-=1

        print("Wrong")
        print(f"You have {turns} more guesses")
        if turns == 0:
            print("You Loose")

        

