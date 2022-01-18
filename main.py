
from data import menu,resources

ml = 'ml'
g = 'g'
dollar = '$'

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

profit = 0


def print_report():
    print('the current resource values are')
    print(f'Water: {water}{ml}')
    print(f'Milk : {milk}{ml}')
    print(f'Coffee : {coffee}{g}')
    print(f'Money : {profit}{dollar}')


def check_resources(coffee_type):
    global water, milk, coffee
    if coffee_type == 'espresso':
        if water >= menu['espresso']['ingredients']['water']\
                and coffee >= menu['espresso']['ingredients']['coffee']:
            return True
        else:
            return False
    elif coffee_type == 'latte':
        if water >= menu['latte']['ingredients']['water'] \
                and coffee >= menu['latte']['ingredients']['coffee'] \
                and milk >= menu['latte']['ingredients']['milk']:
            return True
        else:
            return False
    elif coffee_type == 'cappuccino':
        if water >= menu['cappuccino']['ingredients']['water'] \
                and coffee >= menu['cappuccino']['ingredients']['coffee'] \
                and milk >= menu['cappuccino']['ingredients']['milk']:
            return True
        else:
            return False


def ask_coins():
    print('Please insert coins.')
    penny = float(input('how many pennies ? : ')) * 0.01
    nickles = float(input('how many nickles ? : ')) * 0.05
    dimes = float(input('how many dimes ? : ')) * 0.01
    quarters = float(input('how many quarters ? :')) * 0.25
    return [penny, nickles, dimes, quarters]


def cal_coins(coins_list):
    return sum(coins_list)


def deduct_used_resources(coffee_drink):
    global water, milk, coffee
    for k, v in menu[coffee_drink]['ingredients'].items():
        if k == 'water': water -= v
        elif k == 'milk': milk -= v
        elif k == 'coffee': coffee -= v


serveCoffee = True

while serveCoffee:
    userCoffee = input('What would you like? (espresso/latte/cappuccino) ? :').lower()
    if userCoffee == 'off':
        break
    elif userCoffee == 'report':
        print_report()
    elif check_resources(userCoffee):
        coin_value = cal_coins(ask_coins())
        if coin_value < menu[userCoffee]['cost']:
            print('Sorry that\'s not enough money. Money refunded.')
        elif coin_value >= menu[userCoffee]['cost']:
            if coin_value > menu[userCoffee]['cost']:
                profit += menu[userCoffee]['cost']
                deduct_used_resources(userCoffee)
                print(f'here is ${round(coin_value - menu[userCoffee]["cost"], 2)} in change')
                print(f'Here is your {userCoffee}. 🍺 Enjoy!')
            elif coin_value == menu[userCoffee]['cost']:
                profit += menu[userCoffee]['cost']
                print(f'Here is your {userCoffee}. 🍺 Enjoy!')
    else:
        print('Sorry there is not enough resources to make your coffee.')


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])








