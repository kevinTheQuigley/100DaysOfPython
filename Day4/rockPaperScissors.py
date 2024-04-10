import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS = [rock,paper,scissors]

print("Hi! And welcome to rock paper scissors! Are you ready?")


userChoice = input("What do you choose? Select 0 for rock, 1 for paper and 2 for scissors:\n")

print(userChoice)
#userChoice = int(userChoice1)
if(userChoice== "0"):
    print(f"you have choosen rock! {RPS[0]}")
elif(userChoice == "1"):
    print(f"you have choosen paper! {RPS[1]}")
elif(userChoice == "2"):
    print(f"you have choosen scissors! {RPS[2]}")
else:
    print("you have choosen a value outside of the range. \n please choose either 0,1 or 2")
compChoice = rd.randint(0,2) 
compChoice  = str(compChoice)

if(compChoice== "0"):
    print(f"The computer has choosen rock! {RPS[0]}")
    #if(userChoice== "0"):
    #    print(f"you have drawn! {RPS[0]}")
    #elif(userChoice == "1"):
    #    print(f"you have choosen paper! {RPS[1]}")
    #elif(userChoice == "2"):
    #    print(f"you have choosen scissors! {RPS[2]}")
elif(compChoice== "1"):
    print(f"The computer has choosen paper! {RPS[1]}")
elif(compChoice== "2"):
    print(f"The computer has choosen scissors! {RPS[2]}")
else:
    print("You have choosen a value outside of the range. \n Please choose either 0,1 or 2")
    exit()

#print(f"The computer has choosen {RPS[compChoice]}")

compChoice = int(compChoice)
userChoice = int(userChoice)

if (userChoice == compChoice):
    print("You have drawn!")
elif ((userChoice+1)% 3 == compChoice):
    print("You have lost")
elif ((compChoice +1)% 3 == userChoice):
    print("You have won")
else:
    print("uh oh something is wrong with my calculations!")