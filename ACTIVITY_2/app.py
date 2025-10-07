from controller.rates import Rates

while True:

    print("==============================")
    print("FX APP  (FOREIGN EXCHANGE APP)")
    print("==============================")
    print()
    print("OPERATIONS:")
    print("[1] View Available Rates")
    print("[2] Convert Money")
    print()
    print("Press Any Key to Exit")
    print()

    option = input("Option: ")

    if option == "1":
        Rates().display_rates()
        
    elif option == "2":
        try:
            source_currency = input("Source Currency: ").upper()
            target_currency = input("Target Currency: ").upper()
            amount = float(input("Amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                Rates().convert_rates(source_currency, target_currency, amount)
        except Exception:
            print("Invalid Input. Please enter a valid currency and amount.")

    else:
        break
