word="Python"
guessed=""
chances=5

print("Welcome to hangman game !")
while chances>0:
    display=""
    
    for letter in word:
        if letter in guessed:
            display+=letter
            
        else:
            display+="_"
            
    print("Word :",display)
    if display==word:
        print("You Win !")
        break
    guess=input("Guess a letter :")
    guessed+=guess
    
    if guess not in word:
        chances-=1
        print("Wrong Guess !")
        print("Chances left :",chances)
        
if chances==0:
    print("You lost !")
    print("Word Was :",word)