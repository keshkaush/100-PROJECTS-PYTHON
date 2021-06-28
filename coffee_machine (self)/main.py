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


art = """         / /~~~~~~~~/|
        / /######/ / |
       / /______/ /  |
      ============ /||
      |__________|/ ||
       |\__,,__/    ||
       | __,,__     ||
       |_\====/%____||   
       | /~~~~\ %  / |
      _|/      \%_/  |
     | |        | | /
     |__\______/__|/
    ~~~~~~~~~~~~~~"""


def get_coins(cost):
    penny = int(input("Number of pennies : "))
    nickle = int(input("Number of nickle : "))
    dime = int(input("Number of dime : "))
    quarter = int(input("Number of quarter : "))
    total = penny * 0.01 + nickle * 0.05 + dime * 0.1 + quarter * 0.25
    change = round(total - cost, 2)
    if total >= cost:
        return f"You get the change of ${change}"
    else:
        return "You Don't have enough coin, Coins are getting refunded"


def choice_checker(coffee_type):
    data = MENU[coffee_type]

    cost = data["cost"]

    required_water = data["ingredients"]["water"]
    required_milk = data["ingredients"]["milk"]
    required_coffee = data["ingredients"]["coffee"]

    available_coffee = resources["coffee"]
    available_water = resources["water"]
    available_milk = resources["milk"]

    if required_coffee > available_coffee or required_water > available_water or required_milk > available_milk:
        return "There is not  enough resources in the machine."
    else:
        available_milk -= required_milk
        available_water -= required_water
        available_coffee -= required_coffee
        print(cost)
        return get_coins(cost)


is_off = False

while not is_off:
    print(art)
    choice = input("What would you like, espresso, latte or cappuccino : ")

    if choice == "report":
        for k, v in resources.items():
            print(f"{k} : {v}")
    elif choice == "off":
        is_off = True
    else:
        result = choice_checker(choice)
        print(result)

