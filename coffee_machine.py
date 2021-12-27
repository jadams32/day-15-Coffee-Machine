# For day 15 of 100 days of code I create a coffee machine that asks the user for a drink, takes in their money
# and keeps track of profit, and resources left. Feel free to look around my code and play with the machine. Also don't
# forget the secret words "Report" and "Off" to see the resources left and to turn off the machine!

# Importing necessary modules and data.
import sys
from coffee_data import menu, resources
from art import logo

# Prints the logo to the user
print(logo)

# Setting a global variable for the profit collected by the machine.
profit_collected = 0


def return_change():
    """Returns the customers change if more than the drink cost is inserted."""
    change = format(total_inserted - selected_drink_cost, '.2f')
    print(f"Here is ${change} in change")


def make_coffee(customer_drink_selection, selection_ingredients):
    """Takes the customers drink selection, deducts its resources from the machine and gives the customer their drink"""

    for item in selection_ingredients:
        resources[item] -= selection_ingredients[item]
    print(f"Here's your {customer_drink_selection}. Enjoy!")


def show_report():
    """Shows how many Resources are left, and the profit the machine has taken in."""

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
    """Returns True if enough ingredients, and False otherwise"""

    for item in selection_ingredients:
        if selection_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


# While the machine still has resources we will be able to ask the user for a drink
while resources != 0:

    # Ask the user for their drink selection
    customer_drink_selection = input("What drink would you like today? (espresso/latte/cappuccino): ").lower()

    # If "report" is entered show user the report, if "off" is entered, quit the program.
    if customer_drink_selection == "off":
        sys.exit()
    elif customer_drink_selection == "report":
        show_report()

    # If customer actually selects a drink, run the following
    else:
        # This stores the users drink cost and drink ingredients into usable variables
        selected_drink_cost = menu[customer_drink_selection]["cost"]
        selection_ingredients = menu[customer_drink_selection]["ingredients"]

        # If the machine has enough resources for the drink requested, run the code below.
        if enough_resources(selection_ingredients):
            # Print the cost of the user drink selection, then ask for the user to input coins
            print(f'A(n) {customer_drink_selection} is ${selected_drink_cost}')
            total_inserted = accept_money()

            # The following gives the user a drink if the users inserts the exact amount to purchase the drink
            if total_inserted == selected_drink_cost:
                profit_collected += selected_drink_cost
                make_coffee(customer_drink_selection, selection_ingredients)

            # If the users inserts more than the amount to purchase the drink, change is refunded and drink issued.
            elif total_inserted > selected_drink_cost:
                return_change()
                profit_collected += selected_drink_cost
                make_coffee(customer_drink_selection, selection_ingredients)

            # If the users inserts less than the amount to purchase the drink the user is refunded and no drink is given
            elif total_inserted < selected_drink_cost:
                print("Sorry that's not enough money. Money refunded.")
