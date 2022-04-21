import random
from turtle import right
from unicodedata import category
import colorama
from colorama import Fore, Back
from re import S

import json
# Load the list of words
filehandle = open("words.json")
wordlist = json.load(filehandle)

wrongletters = ""
rightletters = ""

nextword = -1
print(Back.WHITE)

def rules():
    print(Fore.RED + "\nWorldes and Dragons!!!" + Fore.BLACK)
    print("\n********************************************************************************")
    print("Welcome to Wordles and Dragons, a wordle game with words insprired by Dungeons and Dragons.") 
    print("To win you will need to guess three words, you will have five guesses per word")
    print("Guesses will not be limited to five character words.")
    print("Each wrong guess will deal damage depending on the number of unique wrong letters in your input compared to the chosen word")
    print("Damage will also be dealt if your input is shorter or longer than the chosen word. One damage will be dealt, no matter the difference between the two words")
    print("Example, if the word is dragon and you input dwarf, you would take 3 damage. Two damage because w and f from dwarf are not in dragon and one damage because dwarf is a shorter word than dragon")
    print("After the end of each correct guess you will be healed for 10 HP")
    print("At the end of five guesses, if you have not guessed the correct word you will be moved on to another word with your current HP")
    print("Guesses are not case-sensitive")
    print("For each guess, a list of letters will be updated.")
    print("If a letter is green it is in the word, if a letter is red it is not in the word, if a letter is black it was not in your input and was not checked with the chosen word")
    print("*********************************************************************************\n")

# Takes a list of words, and returns one of them, without repeating.


def randomword():
    global nextword, wordlist
    # Shuffle all the words, but only the first time this is called!
    if nextword == -1:
        random.shuffle(wordlist)
    # Return the next word in the list
    nextword += 1
    return wordlist[nextword]


hp = 20


def hpbox():
    print("\nYour current HP is " + str(hp)+ "\n")


def keylist():
    output = ""
    for characternumber in range(ord('A'), ord('Z') + 1):
        character = chr(characternumber)
        if character in wrongletters:
            output = output + Fore.RED + character + Fore.BLACK + " "
        elif character in rightletters:
            output = output + Fore.GREEN + character + Fore.BLACK + " "
        else:
            output = output + character + " "
    print(output)


def guess():
    guess = input("Enter a D&D related word: ")
    return guess

def resetattempt():
    global rightletters, wrongletters
    rightletters = ""
    wrongletters = ""

def check (useranswer, correctanswer):
    if useranswer.upper() == correctanswer['word'].upper():
        print(useranswer + " was the correct Answer good job!\n\n")
        return True
    damage = 0
    if len(useranswer) > len(correctanswer['word']):
        print ("SMACK! Your answer was too long")
        damage += 1
    elif len(useranswer) < len(correctanswer['word']):
        print("STABBY STAB! Your answer was too short!")
        damage += 1
    else:
        print("Nice! Correct length")
    global hp
    hp -= damage
    letterdiff(correctanswer, useranswer)
    print("Sorry, try again")
    return False

def letterdiff(correctanswer, useranswer):
    damage = 0
    global wrongletters, rightletters
    for i in range(len(useranswer)):
        letter = useranswer[i].upper()
        # if the current letter is NOT in the answer word, add one to damage
        if not letter in correctanswer['word'].upper():
            print(letter + " is not in the answer!")
            damage += 1
            if not letter in wrongletters:
                wrongletters = wrongletters + letter
        else:
            rightletters = rightletters + letter
    # print ("Damage per letterdiff is " + str(damage))
    global hp
    hp = hp - damage
    if hp <= 0:
        print("The Dragon killed you, game over!")
        quit()

def hint(guessno, correctword):
    if guessno == 3:
        print("The word is a " + correctword['category'])

def update(correctanswer):
    if correctanswer:
        global hp
        hp += 10
        # print(hp)