import sys

from coffee_data import menu, resources
from art import logo


print(logo)


profit_collected = 0


def return_change():
    change = format(total_inserted - selected_drink_cost, '.2f')
    print(f"Here is ${change} in change")


def make_coffee(customer_drink_selection, selection_ingredients):

    for item in selection_ingredients:
        resources[item] -= selection_ingredients[item]
    print(f"Here's your {customer_drink_selection}. Enjoy!")


def show_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f"Money: ${profit_collected}")


def accept_money():
    """Asks the user for coin input and returns the total"""

    print("Please Insert Coins")
    inserted_quarters = float(input("How many quarters?: ")) * .25
    inserted_dimes = float(input("How many dimes?: ")) * .10
    inserted_nickels = float(input("How many nickels?: ")) * .05
    inserted_pennies = float(input("How many pennies?: ")) * .01

    total = inserted_quarters + inserted_dimes + inserted_nickels + inserted_pennies
    return total


def enough_resources(selection_ingredients):
    for item in selection_ingredients:
        if selection_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


while resources != 0:

    customer_drink_selection = input("What drink would you like today? (espresso/latte/cappuccino): ").lower()
    # print(menu[customer_drink_selection]["ingredients"])
    if customer_drink_selection == "off":
        sys.exit()
    elif customer_drink_selection == "report":
        show_report()
    else:

        selected_drink_cost = menu[customer_drink_selection]["cost"]
        selection_ingredients = menu[customer_drink_selection]["ingredients"]

        if enough_resources(selection_ingredients):
            print(f'A(n) {customer_drink_selection} is ${selected_drink_cost}')
            total_inserted = accept_money()
            if total_inserted == selected_drink_cost:
                profit_collected += selected_drink_cost
                make_coffee(customer_drink_selection, selection_ingredients)

            elif total_inserted > selected_drink_cost:
                return_change()
                profit_collected += selected_drink_cost
                make_coffee(customer_drink_selection, selection_ingredients)

            elif total_inserted < selected_drink_cost:
                print("Sorry that's not enough money. Money refunded.")
