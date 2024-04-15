from sys import platform
import data
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


MENU = data.MENU
RESOURCES = data.resources
TURNEDON = True
# TODO Define resources update function

# TODO Define the while that checks data availability

# TODO Define input function

def checkResources(userInput):
    """Checks if enough resources have been inserted for the coffee selected"""
    global RESOURCES
    global MENU

    print(userInput)
    print(MENU[userInput]["ingredients"])
    if (not "milk" in MENU[userInput]["ingredients"].keys()):
        MENU[userInput]["ingredients"]["milk"] = 0
    for key in MENU[userInput]["ingredients"]:
        if int(MENU[userInput]["ingredients"][key]) > int(RESOURCES[key]):
            print(f"Unfortunately, we are out of {key}. Please come back later.")
            return(False)
        return(True)



        
def checkCoins(userInput):
    """Checks if the user has inserted enough coins"""
    cost = MENU[userInput]["cost"]
    quarters = int(input("How many quarters?"))
    pennies = int(input("How many pennies?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    totalMoney = (quarters*0.25 + dimes*0.1+pennies*0.01+nickles*0.05)
    remainder = totalMoney - cost
    if remainder >0:
        print(f"Your change is {remainder}")
        return True
    else:
        print(f"I'm sorry, you have not inserted enough money. Please take your change of {totalMoney}")
        return False

def adjustResources(userInput):
    global RESOURCES
    for key in MENU[userInput]["ingredients"].keys():
        RESOURCES[key] = RESOURCES[key] - MENU[userInput]["ingredients"][key]
    #print(f"Current resources are \n {RESOURCES}")
    RESOURCES["money"] = MENU[userInput]["cost"]

    





def takeInput():
    global TURNEDON 
    userInput = input("Hi! What kind of coffee would you like? Espresso/Americano/Latte \n").lower()
    if userInput == "off":
        turnedOn = False
    elif userInput == "report":
        print(f"The current resources available are:- \n{RESOURCES}")
    elif userInput in ["latte","espresso","americano"]:
        enoughResources = checkResources(userInput)
        if not enoughResources:
            return False
        enoughChange = checkCoins(userInput)
        if enoughChange:
            adjustResources(userInput)
        print(f"Enjoy your {userInput}🍵!")




    

TURNEDON= True
while TURNEDON ==True:
    takeInput()