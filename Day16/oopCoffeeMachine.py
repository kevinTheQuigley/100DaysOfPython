from coffeeMachineObjects import CoffeeMaker
from coffeeMachineObjects import MenuItem
from coffeeMachineObjects import Menu
from coffeeMachineObjects import MoneyMachine

coffeeMachine = CoffeeMaker()
#latte = MenuItem("latte",100,100,100,1)
#espresso = MenuItem("espresso",100,100,100,1)
#americano= MenuItem("americano",100,100,100,1)
theMenu = Menu()



coffeeMachine.report()

#coffeeMachine.is_resource_sufficient("latte")

print(theMenu.get_items())