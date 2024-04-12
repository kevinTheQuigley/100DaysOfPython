from sys import platform
import artFile
import os
#clear = lambda: os.system('cls') #on Windows System
#os.system('clear') #on Linux System
#clear()

def is_platform_windows():
    return platform == "win32"
if is_platform_windows():
    clear = lambda: os.system('cls') #on Windows System
else:
    lambda: os.system('cls') #on Windows System
clear()

print(artFile.logo)
auctionOn = True
bidDict = {}

while(auctionOn ==True):
    print("Welcome to the auction bidder!")
    name = input("What is your name?: ")
    bid = input("What would you like to bid?: ")
    bidDict[name] = bid
    bidders = input("Are there any other bidders? Please type \"Yes\" or \"No\"").lower()
    print(bidders)
    if bidders == "no":
        auctionOn =False
        clear()
    else:
        clear()
bidList = list(di.values())
winBid=max(list(bidDict.values()))
bidList.index(bidList)
print("The winning bid is $"+winBid+".")


    


