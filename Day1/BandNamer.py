#print("Hi and welcome to my band namer program")
#var = input("What is the name of the city where you born?\n")
#print(var)

#num1=1
#print("Yo"+ 
#      input("what's your name cunt?")
#    )
#
#print("what the"+input())
import sys

# Extracting command-line arguments
city_input = sys.argv[1] if len(sys.argv) > 1 else input("Please enter the city where you were born:\n ")
pet_input = sys.argv[2] if len(sys.argv) > 2 else input("Please enter your pets name:\n ")

# Printing the inputs
print("Your bands name will be "+city_input+"'s "+pet_input+"s")