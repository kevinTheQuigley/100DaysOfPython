#TipCalculator

print("Welcome to the tip calculator!")

bill = input("What was the total bill? :$")

tip = input("How much of a tip would you like to give? ie 10%, 12% or a cheeky nothing?: %")

people = input("How many people would you like to split the bill with? :")

totalBill = int(bill)+int(bill)*float(tip)/100

perPerson = totalBill/int(people)

print(f"The total amount per person is ${perPerson} per person.")

