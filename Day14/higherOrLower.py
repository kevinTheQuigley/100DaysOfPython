from sys import platform
import art
import os
import random
import gameData
#clear = lambda: os.system('cls') #on Windows System
#os.system('clear') #on Linux System
#clear()

def is_platform_windows():
    return platform == "win32"
if is_platform_windows():
    clear = lambda: os.system('cls') #on Windows System
else:
    lambda: os.system('cls') #on Windows System

gameOver = False


def generateSentance(digit):
    i = random.randint(0,len(gameData.data)-1)
    dataDict = gameData.data[i]
    name = dataDict["name"]
    job = dataDict["description"]
    country = dataDict["country"]
    print(f"Compare {digit}: {name}, a {job} from {country}.")
    return(dataDict["follower_count"])


def game(score):
    clear()
    print(art.logo)
    if score>0:
        print(f"You are correct! Well done, your current score is {score}")
    scoreA = int(generateSentance("A"))
    print(art.vs)
    scoreB = int(generateSentance("B"))
    userGuess = input("Please guess either A or B: ").lower()
    if ((scoreA >scoreB) and (userGuess =="a")) or ((scoreB> scoreA) and (userGuess =="b")):
        score +=1
        game(score)

    else:
        return incorrectGuess()


def incorrectGuess():
    clear()
    print(art.logo)
    print("I'm sorry, you have guessed incorrectly. Your final score was {score}.\n")
    cont =input(" Would you like to play again?\n y/n:- ").lower()
    score = 0
    if cont=="n":
        return True
    elif cont== "y":
        game(score)
        return False
    else:
        print(" I'm sorry, invalid input")

gameOver = False


while gameOver == False:
    score =0
    gameOver =game(score)