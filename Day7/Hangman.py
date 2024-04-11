#Hangman
import random as rd
import HangmanWords
import HangManArt

#word_list = ["banana","bookkeeper","sausages","delicious"]
word_list= HangmanWords.word_list
chosen_word = word_list[rd.randint(0,len(word_list)-1)]


letStr = "abcdefghijklmnopqrstuvwxyz"
global guessString
guessString = ""

def giveInput(guessString):
    guess = input("Guess a letter?\n ").lower()
    print(guessString)
    while guess in guessString:
        guess = input("You've guessed that letter already! Please try anaother.\n")
    while not guess in letStr:
        guess = input("I'm sorry, this letter isn't in the alphabet Can you please guess again?\n ")
    guessString =guessString+guess
    return [guess,guessString]

gameOver = False
Win = False
winCount = len(chosen_word)
looseCount = 6
winCounter = 0
looseCounter = 0
winBlank = []
for i in range(winCount):
    winBlank.append( "-")
print(winBlank)

def updateWinBlank(winBlank,guess,choosen_word,winCounter):
    for i in range(winCount):
        if (guess == choosen_word[i]):
            winBlank[i]= guess
            winCounter+=1
    return winCounter

while gameOver == False:
    [guess,guessString] = giveInput(guessString)
    if guess in chosen_word:
        print("You got a guess right!\n")
        winCounter = updateWinBlank(winBlank,guess,chosen_word,winCounter)
        print(winBlank)
    else:
        print("Uh oh, that's wrong!")
        looseCounter+=1
    if (looseCount == looseCounter+1) or (winCount == winCounter):
        gameOver = True

if (looseCount == looseCounter+1):
    print("You loose")
elif (winCount == winCounter+1):
    print("You win")
