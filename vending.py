def display_menu():
    print("Welcome to the Vending Machine!")
    print("Please select an item by entering the corresponding number or name:")
    print("1. Cola - $1.25")
    print("2. Diet Cola - $1.00")
    print("3. Cola Zero - $1.25")
    print("4. Chocolate Bars - $2.00")
    print("5. Chips - $1.50")

def get_price(selection):
    menu = {
        "1": 1.25, "cola": 1.25,
        "2": 1.00, "diet cola": 1.00,
        "3": 1.25, "cola zero": 1.25,
        "4": 2.00, "chocolate bars": 2.00,
        "5": 1.50, "chips": 1.50
    }
    if selection.lower() in menu:
        return menu[selection.lower()]
    else:
        return None

def vending_machine():
    display_menu()
    valid_selection = False
    while not valid_selection:
        selection = input("Enter your selection: ")
        price = get_price(selection)
        if price is not None:
            valid_selection = True
        else:
            print("Invalid selection. Please try again.")
    
    valid_amount = False
    while not valid_amount:
        try:
            money_entered = float(input(f"The price is ${price}. Please enter the amount of money you are inserting: "))
            if money_entered >= price:
                change = money_entered - price
                print(f"Thank you! Here is your {selection} and your change is ${change:.2f}.")
                valid_amount = True
            else:
                print(f"Insufficient amount. Please enter at least ${price}.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

if __name__ == "__main__":
    vending_machine()
