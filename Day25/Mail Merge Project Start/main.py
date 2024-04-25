#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt","r") as start:
    text = start.read()

f = open("./Input/Names/invited_names.txt","r")
names = f.readlines()
for i in range(len(names)) :
    names[i] = names[i].strip()

letterList = []
for name in names:
    letterList.append(text.replace("[name]",name))

for i in range(len(names)) :
    with open("./Output\\ReadyToSend/"+names[i],"w") as output:
        output.write(letterList[i])

print(letterList[0])