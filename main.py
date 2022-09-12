from menu import *

total_earned = 0

coffee_machine = True


def enough_ingredients(client_ingredient):
    """
    Checks that the coffee machine has enough ingredients to make the user's drink
    :param client_ingredient:
    :return: lets the user know if there's not enough ingredients or if there is, how much they need to pay
    """
    for item in client_ingredient:
        if resources[item] < client_ingredient[item]:
            print(f"Sorry there is not enough {item}.")
            return True


def counting_coins():
    """
    Takes input from the user to calculate total of money
    :return: The sum of all the money users have
    """
    print(f"Please insert {choice['cost']}")
    total = 0
    number_of_coins = int(input("How many coins do you have? "))
    for n in range(number_of_coins):
        coin_type = input("What coins are you inserting? ")
        total += coins[coin_type]
    return total


def paying_bill(payment):
    """
    Calculates if the user has got enough money to make the purchase and whether they need to get change
    :param: payment, an integer with the total money the user has inserted.
    :return: a print statement confirming whether the user can complete the purchase
    """
    if payment < choice['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment == choice['cost']:
        global total_earned
        total_earned += choice['cost']
        return True
    else:
        total_earned += choice['cost']
        print(f"Here is your change: {round(payment - choice['cost'], 2)}$")
        return True


def make_coffee(customer_order, drink):
    """
    Returns the updated quantity of the resources
    :param customer_order: item entered by user
    :param drink: ingredients used to make the drink
    :return: the confirmation of the order and the resources are updated.
    """
    for item in choice['ingredients']:
        resources[item] -= drink[item]
    print(f"Here's your {customer_order}")


# Main App Logic
while coffee_machine:
    customer_order = input("What would you like to drink? (Espresso/Latte/Cappuccino) ").lower()
    if customer_order == "report":
        print(f"Resources: {resources['water']}ml, {resources['milk']}ml, {resources['coffee']}g. "
              f"Total Payment: {total_earned}")
    elif customer_order == "off":
        coffee_machine = False
        print("Thanks for using this machine")
    else:
        choice = MENU[customer_order]
        if not enough_ingredients(choice["ingredients"]):
            payment = counting_coins()
            if paying_bill(payment):
                make_coffee(customer_order, choice["ingredients"])







