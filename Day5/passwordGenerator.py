
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Qevs Password Generator!\n This generator is 100% safe and gaurenteed secure")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letList = []
symList= []
numList = []
for num in range(0,nr_letters):
    let = letters[random.randint(0,len(letters)-1)]
    letList.append(let)
#print(letList)
letList = "".join(letList)

for num in range(0,nr_symbols):
    let = symbols[random.randint(0,len(symbols)-1)]
    symList.append(let)

symList = "".join(symList)

for num in range(0,nr_numbers):
    let = numbers[random.randint(0,len(numbers)-1)]
    numList.append(let)

numList = "".join(numList)

totalList = []
totalList.append(letList)
totalList.append(numList)
totalList.append(symList)

totalList = "".join(totalList)
print("This is the unrandomized list\n"+totalList)

listLength = len(totalList)
newStr = ""
counter = listLength
for i in range(0,listLength):
    rd = random.randint(0,counter-1) 
    rLet = totalList[rd]
    newStr += rLet
    totalList = totalList.replace(rLet, '', 1)
    counter = counter -1 

print("This is the randomized list\n"+newStr)
print('''
       .------..
     -          -
   /              \
 /                   \
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O     Uhhh, this computer
  \      _____      /       is like, busted or
    \ ( /#####\ ) /       something. So go away.
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\
     /           \
   /               \
  /__|  AC / DC  |__\
  | ||           |\ \
''')