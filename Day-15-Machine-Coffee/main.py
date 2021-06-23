from ressources import MENU, resources


# TODO 1. Print report
def stat_machine_coffee():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")


# TODO 2. Check resources sufficient
def check_ressources(choice):
    ingredients = MENU[choice]['ingredients']
    water_required = ingredients['water']
    coffee_required = ingredients['coffee']
    if "milk" in ingredients:
        milk_required = ingredients['milk']
    else:
        milk_required = 0
    if resources['water'] >= water_required:
        if resources['coffee'] >= coffee_required:
            if resources['milk'] >= milk_required:
                return True
            else:
                coffee()
                print("There is not enough milk. ")

        else:
            coffee()
            print("There is not enough coffee.")
    else:
        coffee()
        print("There is not enough water.")


# TODO 3. Process coins and # TODO 4. Check transaction successful
def processing_coins(choice, quarters, dimes, nickels, pennies):
    """Process coins and Check transaction successful and return True or False"""
    price = MENU[choice]['cost']
    quarters *= 0.25
    dimes *= 0.1
    nickels *= 0.05
    pennies *= 0.01
    total = quarters + dimes + nickels + pennies
    if total >= price:
        print(f"Here is ${total - price} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        coffee()
        return False


# TODO 5. Make coffee
def make_coffee(drink):
    """Take the transaction report, the drink and making coffee by subtracting
    resources consumed """
    coffee = MENU[drink]
    ingredients = coffee['ingredients']
    water_consumed = ingredients['water']
    coffee_consumed = ingredients['coffee']
    if "milk" in ingredients:
        milk_consumed = ingredients['milk']
    else:
        milk_consumed = 0

    resources['water'] -= water_consumed
    resources['milk'] -= milk_consumed
    resources['coffee'] -= coffee_consumed
    print(f"Here is your {drink} enjoy !")


def coffee():
    continue_serving = True

    while continue_serving:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            stat_machine_coffee()
            pass
        elif choice == 'off':
            continue_serving = False
            break
        else:
            check_ressources(choice)
        coffee()

        print("Please insert coins.")
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))

        is_transaction_done = processing_coins(choice, quarters, dimes, nickels, pennies)
        if is_transaction_done:
            make_coffee(choice)


coffee()
