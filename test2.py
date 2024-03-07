def british_pound_to_aed(amount):
    '''
    This function simply converts from GBP to AED by multiplying the given amount by the GBP_TO_AED constant
    - Ribal Bou Ghanem
    '''
    GBP_TO_AED = 4.66 # This is the conversion rate from british pound to AED
    converted = round(amount * GBP_TO_AED, 2)
    return converted

def dollar_to_aed(amount):
    '''
    This function simply converts from USD to AED by multiplying the given amount by the USD_TO_AED constant
    - Ribal Bou Ghanem
    '''
    USD_TO_AED = 3.67 # This is the conversion rate from dollars to AED
    converted = round(amount * USD_TO_AED, 2)
    return converted

def aed_to_dollar(amount):
    '''
    This function simply converts from AED to USD by multiplying the given amount by the AED_TO_USD constant
    - Ribal Bou Ghanem
    '''
    AED_TO_USD = 0.27 # This is the conversion rate from AED to dollars
    converted = round(amount * AED_TO_USD, 2)
    return converted

def choice2(amount):
    '''
    This function contains a secondary if statement that will be executed only if the user chooses 2 as a choice in the function main()
    - Ribal Bou Ghanem
    '''
    target_currency = ""
    while target_currency != 1 and target_currency != 2 and target_currency != 3: #This loop will keep repeating until the user enters 1, 2, or 3 
        print("\n1. Euro to AED (EUR)\n2. British Pound to AED (GBP)\n3. US Dollar to AED\n")
        target_currency = int(input("Enter the target currency from the above menu- choice (1/2/3): "))
        if target_currency == 1:
            pass # Sarah is responsible for Euro to AED function and I do not have this yet so I will pass this part for now
        elif target_currency == 2:
            print(f"{amount} GBP is equal to {british_pound_to_aed(amount)} AED")
        elif target_currency == 3:
            print(f"{amount} USD is equal to {dollar_to_aed(amount)} AED")
        else:
            print("Invalid amount") # If the user chooses a choice other than 1, 2, or 3 then this will be printed and user will be met with the same menu

def main():
    '''
    This function contains while loops with if statements within to execute functions based on the user's input
    - Ribal Bou Ghanem
    '''
    choice = ""
    while choice != 3: # The loop will keep repeating unless the user chooses 3 as the choice when given the menu
        choice = ""
        while choice != 1 and choice != 2 and choice != 3: # This loop is made to make sure that if the user does not enter a valid choice the if statements will continue to work when given the menu again
            choice = int(input("Enter the conversion direction- choice (1/2/3): "))
            if choice == 1:
               pass # Sarah is responsible for creating the function choice1() so I will add this once I have it soon
            elif choice == 2:
                amount = float(input("Enter the amount you want to convert: "))
                choice2(amount)
            elif choice == 3:
                print("Bye!!")
                break
            else:
                print("Invalid choice") # If the user enters an invalid choice then this string will be printed and the loops will repeat

if __name__ == "__main__":
    main()
