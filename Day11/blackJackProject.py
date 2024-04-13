############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

from sys import platform
import art
import os
import random
#clear = lambda: os.system('cls') #on Windows System
#os.system('clear') #on Linux System
#clear()

def is_platform_windows():
    return platform == "win32"
if is_platform_windows():
    clear = lambda: os.system('cls') #on Windows System
else:
    lambda: os.system('cls') #on Windows System

cardList = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
userPlays = True
anotherCard = False
def chooseCard():
    return(cardList[random.randint(0,12)])

def initialHand():
    hand = []
    hand.append(chooseCard())
    hand.append(chooseCard())
    return(hand)

def getTotal(tHand):
    total = 0
    aceCounter =0
    for card in tHand:
        if card in "JQKA":
            val = 10
            total+=val
        else:
            total+=int(card)
        if card =="A":
            aceCounter+=1
    if (aceCounter >0)and (total>21):
        total -=10
    return(total)

def addCard(hand):
    print(f"Your hand is {hand}")
    if (getTotal(hand)>21):
        rHand = hand
        print(rHand)
        return(rHand)
    anotherCard = input("Would you like to take another card?\n\"y\" or \"n\":").lower()
    if anotherCard=="n" :
        return(hand)
    elif anotherCard== "y":
        hand.append(chooseCard())
        hand = addCard(hand)
        return(hand)
    else:
        print("Please enter a viable input")
        hand = addCard(hand)
        return(hand)


def genComputerCards():
    cards = initialHand()
    print(f"The first card generated for the computer is {cards[0]}")
    return (cards)

def addComputerCard(hand):
        hand.append(chooseCard())
        return(hand)

def addComputerCards(computerCards,userCards):
    while (getTotal(computerCards) <19) or (getTotal(computerCards)<getTotal(userCards)):
        computerCards = addComputerCard(computerCards)
        print("The dealer has taken another card")
    return(computerCards)



while userPlays == True:
    clear()
    print(art.logo)
    computerCards = genComputerCards()

    userCards = initialHand()
    userCards = addCard(userCards)
    if getTotal(userCards) > 21:
        print("You went over. You loose.:( ")
    elif getTotal(computerCards) <getTotal(userCards):
        computerCards = addComputerCards(computerCards,userCards)
    print(f"The final computer cards are {computerCards}, and their total is {getTotal(computerCards)}\n")
    if getTotal(computerCards) <getTotal(userCards) or getTotal(computerCards)>21:
        print("You win! Congratulations :D")
    elif getTotal(computerCards) >getTotal(userCards)  and getTotal(computerCards)< 22:
        print("You loose, the computer had beaten you :(")










    #This line should be last

    playGame = input("Would you like to play a new game?\n\"y\" or \"n\":").lower()
    if playGame =="n":
        userPlays = False
    elif not playGame == "y":
        playGame = input("Please select either yes or no.\n\"y\" or \"n\":").lower()


    































#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.