import random as rd


def numberGenerator():
    return rd.randint(1,100)

def diff():
    choice = input("Choose a difficulty, either easy(e) or hard(h):\n").lower()
    if choice =="e":
        return 10
    elif choice == "h":
        return 5
    else:
        print("You have not selected e or h!")
        return diff()

def endGame():
    choice = input("Would you like to play again? y/n\n")
    if choice =="y":
        return True
    elif choice == "n":
        return False
    else:
        print("You have not selected y or n!")
        return endGame()

def checkNum(num):
    global chances
    if chances ==0:
        print("Game over, you have run out of guesses! ")
        return()

    guess = int(input("Please give a guess of the number value between 1 and 100\n"))
    if num == guess:
        print(f"Congratulations! You've won the game. The correct number is {num}")
        return()
    elif(num>guess):
        chances -=1
        print(f"Too low! Please guess again! You have {chances} guesses left")
        checkNum(num)
    elif(guess >num):
        chances -=1
        print(f"Too high! Please guess again. You have {chances} guesses left")
        checkNum(num)
    else:
        print("Something has gone wrong. Please contact the overlord")


    

playing = True
while playing ==True:
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    num = numberGenerator()
    global chances
    chances = diff()
    val = checkNum(num)



    playing = endGame()

