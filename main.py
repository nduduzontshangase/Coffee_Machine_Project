MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(item):
    for i in item:
        if resources[i] < item[i]:
            return i


money = 0


def coffee_machine():
    buy_coffee = True
    global money
    while buy_coffee is True:
        customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if customer_order == "report":
            for i in resources:
                if i == "water" or i == "milk":
                    print(f"{i}: {resources[i]}ml")
                elif i == "coffee":
                    print(f"{i}: {resources[i]}g")
            print(f"Money: ${money}")
        elif customer_order == "off":
            buy_coffee = False
        else:
            item = MENU[customer_order]["ingredients"]
            if check_resources(item) == None:
                cost = MENU[customer_order]["cost"]
                print(f"The price of {customer_order} is ${cost}.")
                print("Please insert coins.")

                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickels = int(input("how many nickels?: "))
                pennies = int(input("how many pennies?: "))

                paid = round((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01), 2)
                if paid < cost:
                    print(f"Sorry. Not enough money. Money refunded ${paid}.")
                    coffee_machine()
                change = round(paid - cost, 2)
                money += cost
                print(f"Here is ${change} change.")

                for i in item:
                    new_availability = resources[i] - item[i]
                    resources[i] = new_availability
                    # print(f"{i} = {resources[i]}")
                print(f"Here is your {customer_order} ☕. Enjoy")

            else:
                print(f"Sorry there is not enough {check_resources(item)}")
                coffee_machine()


coffee_machine()
