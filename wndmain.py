from wndfunctions import rules, randomword, hpbox, keylist, guess, check, update, resetattempt, hint
#prints the rules
rules()
#loopstheguesses
currentwordno = 1
totalwordno = 3
maxguesses = 5

# Loop over 3 words
while currentwordno <= totalwordno:
    iscorrect = False
    guessno = 1
    #chooses a random word
    correctword = randomword()
    resetattempt()
    # Loop until the user either guesses the word, runs out of guesses (choose new word) or dies.
    while guessno <= maxguesses and iscorrect == False:
        #prints current hp
        hpbox()
        #prints a list of acceptable keys
        keylist()
        #user input guess
        useranswer = guess()
        print()
        #hint system 3 guesses gives you category four guesses gives you descrption
        #check function compares the input word and the chosen word and prints a message accordingly, if the word is not in the list the player loses a guess
        iscorrect = check(useranswer, correctword)
        hint(guessno, correctword)
        guessno += 1 
        if iscorrect == True:
            if currentwordno == totalwordno:
                print("You win")
                quit()
            else:
                print("You hit the dragon, try another word")        
        elif guessno > maxguesses and iscorrect == False:
            print("The Dragon killed you, try again")
        #update function calculates lost/gained hp,'death', correct/wrong letters, collected letters, colored letters, type hints,and shorter or longer hints
        update(iscorrect)
    if iscorrect == True:
        currentwordno += 1
