#Building a Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))

direction = "encode"
text = "HeyYall"
shift = "5"
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    indexList = []
    for i in range(0,len(text)):
        letter = text[i].lower()

        ind = (alphabet.index(letter) +int(shift))
        if ind >len(alphabet)-1:
            ind = ind - len(alphabet)
        newLetter = alphabet[ind]
        indexList.append(newLetter)
    word = "".join(indexList)

    print(word)

def decrypt(text,shift):
    indexList = []
    for i in range(0,len(text)):
        letter = text[i].lower()

        ind = (alphabet.index(letter) -int(shift)) 
        if ind <0:
            ind = ind + len(alphabet) 
        newLetter = alphabet[ind]
        indexList.append(newLetter)
    word = "".join(indexList)

    print(word)


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
#encrypt(text,shift)
#text2 = "mjddfqq"
#decrypt(text2,shift)

choice = ""
shiftNo = "0"

while ((not choice == "encrypt") or (not choice == "decrypt")) and (not 0<int(shiftNo) ):
    choice = input("Would you like to encrypt or decrypt some text? \nPlease type either \"Encrypt\" or \"Decrypt\": ").lower()
    word = input("What word would you like to encrypt?\n: ")
    shiftNo = input("How much would you like to shift your letters?\n: ")
    print(choice)
    print(shiftNo)
    if (choice == "encrypt"):
        encrypt(word,shiftNo)
    elif(choice=="decrypt"):
        decrypt(word,shiftNo)
    else:
        print("Please give the correct inputs and try again")