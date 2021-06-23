from ressources import MENU, resources


# TODO 1. Print report
def stat_machine_coffee():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")


# TODO 2. Check resources sufficient
def check_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"There is not enough {item} ")
            return False
    return True


# TODO 3. Process coins
def processing_coins():
    """Return the total from inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


# TODO 4. Check transaction successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when the transaction is successful and False if not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        resources['money'] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 5. Make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink} ☕ enjoy !")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        stat_machine_coffee()
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice]
        if check_resource_sufficient(drink["ingredients"]):
            payment = processing_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
