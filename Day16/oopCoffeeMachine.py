from coffeeMachineObjects import CoffeeMaker
from coffeeMachineObjects import MenuItem
from coffeeMachineObjects import Menu
from coffeeMachineObjects import MoneyMachine

coffeeMachine = CoffeeMaker()
#latte = MenuItem("latte",100,100,100,1)
#espresso = MenuItem("espresso",100,100,100,1)
#americano= MenuItem("americano",100,100,100,1)
theMenu = Menu()
coin_machine = MoneyMachine()
is_machine_on = True


while is_machine_on==True:
    user_input = input("Hi and welcome to the OOP coffee machine!\n What kind of coffee would you like?:- ").lower()
    if user_input == "off":
        is_machine_on = False
    elif user_input == "report":
        coffeeMachine.report()
        coin_machine.report()
    else:
        drink = theMenu.find_drink(user_input)
        if coffeeMachine.is_resource_sufficient(drink):
            coin_machine.make_payment(drink.cost)
            print()
            coffeeMachine.make_coffee(drink)

''' 
'''