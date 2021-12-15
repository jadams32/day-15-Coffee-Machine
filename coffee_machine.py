import sys

from coffee_data import menu, resources
from art import logo
from collections import Counter

print(logo)


profit_collected = 0

def show_report():
    print(f"Water: {profit_collected}ml")
    print(f"Milk: {profit_collected}ml")
    print(f"Coffee: {profit_collected}ml")
    print(f"Money: ${profit_collected}")

def make_coffee():
    resources_left = {key: resources[key] - menu[customer_drink_selection].get(key, 0) for key in resources}
    print(resources_left)
    print(f"Here's your {customer_drink_selection}. Enjoy!")


def return_change(total_inserted, selected_drink_cost):
    change = format(total_inserted - selected_drink_cost, '.2f')
    print(f"Here is ${change} in change")


while resources != 0:

    customer_drink_selection = input("What drink would you like today? (espresso/latte/cappuccino): ").lower()
    if customer_drink_selection == "off":
        sys.exit()
    elif customer_drink_selection == "report":
        show_report()
    else:

        selected_drink_cost = menu[customer_drink_selection]["cost"]

        print(f'A(n) {customer_drink_selection} is ${selected_drink_cost}')
        print("Please Insert Coins")
        inserted_quarters = float(input("How many quarters?: ")) * .25
        inserted_dimes = float(input("How many dimes?: ")) * .10
        inserted_nickels = float(input("How many nickels?: ")) * .05
        inserted_pennies = float(input("How many pennies?: ")) * .01

        total_inserted = inserted_quarters + inserted_dimes + inserted_nickels + inserted_pennies

        if total_inserted == selected_drink_cost:
            profit_collected += selected_drink_cost
            make_coffee()

        elif total_inserted > selected_drink_cost:
            return_change(total_inserted, selected_drink_cost)
            profit_collected += selected_drink_cost
            make_coffee()

        elif total_inserted < selected_drink_cost:
            print("Sorry that's not enough money. Money refunded.")

# TODO: 3. Check the resources to determine if enough to make drink
# TODO: 4. If not enough resources prompt user to ask again for type of drink
# TODO: 13. Allow user to check resources with secret word "report"

