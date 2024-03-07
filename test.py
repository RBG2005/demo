""""
GCIS-123-603
    Prof.Ali Assi.
Activity 2:
Group 1:
    Sarah Arab (def validate_input)(def aed_to_euro) (def euro_to_aed) (def main)
    Ribal Bou Ghanem (def aed_to_dollar)(def dollar_to_aed) (def main)

This activity is mainly done using python code language to 
"""


# Constants for conversion rates between AED and other currencies
AED_TO_EURO = 0.25
AED_TO_BRITISH_POUND = 0.21
AED_TO_DOLLAR = 0.27

def validate_input(amount):
    """Validate that the input amount is a positive number."""
    amount = float(amount)
    if amount > 0:
        return True
    else:
        print("Error: The amount must be a positive number.")
        return False

def aed_to_euro(money):
    """Convert AED to Euro."""
    return money * AED_TO_EURO



def aed_to_british_pound(money):
    """Convert AED to British Pound."""
    return money * AED_TO_BRITISH_POUND

def aed_to_dollar(money):
    """Convert AED to US Dollar."""
    return money * AED_TO_DOLLAR

def dollar_to_aed(amount):
    """Convert US Dollar to AED."""
    return amount / AED_TO_DOLLAR

def british_pound_to_aed(amount):
    """Convert British Pound to AED."""
    return amount / AED_TO_BRITISH_POUND

def euro_to_aed(amount):
    """Convert Euro to AED."""
    return amount / AED_TO_EURO

def main():
    """Main function to run the currency converter program."""
    while True:
        print("\nCurrency Converter")
        print("1. Convert AED to other currencies")
        print("2. Convert other currencies to AED")
        print("3. Exit")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            amount = input("Enter the amount you want to convert from AED: ")
            if validate_input(amount):
                amount = float(amount)
                print("\n1. Convert to Euro")
                print("2. Convert to British Pound")
                print("3. Convert to US Dollar")
                print("4. Go back to main menu")
                choice = input("Enter the number of your choice: ")
                if choice == '1':
                    print("You chose to convert AED to Euro.")
                    print("Converted amount: ", aed_to_euro(amount), "EUR")
                elif choice == '2':
                    print("You chose to convert AED to British Pound.")
                    print("Converted amount: ", aed_to_british_pound(amount), "GBP")
                elif choice == '3':
                    print("You chose to convert AED to US Dollar.")
                    print("Converted amount: ", aed_to_dollar(amount), "USD")
                elif choice == '4':
                    continue
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '2':
            amount = input("Enter the amount you want to convert: ")
            if validate_input(amount):
                amount = float(amount)
                print("\n1. Convert from Euro")
                print("2. Convert from British Pound")
                print("3. Convert from US Dollar")
                print("4. Go back to main menu")
                choice = input("Enter the number of your choice: ")
                if choice == '1':
                    print("You chose to convert Euro to AED.")
                    print("Converted amount: ", euro_to_aed(amount), "AED")
                elif choice == '2':
                    print("You chose to convert British Pound to AED.")
                    print("Converted amount: ", british_pound_to_aed(amount), "AED")
                elif choice == '3':
                    print("You chose to convert US Dollar to AED.")
                    print("Converted amount: ", dollar_to_aed(amount), "AED")
                elif choice == '4':
                    continue
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()