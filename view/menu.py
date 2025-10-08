def display_logo():
    print("\n================================")
    print("FX APP  (FOREIGN EXCHANGE APP)")
    print("================================")

def display_options():
    print("\nOPERATIONS:")
    print("[1] View Available Rates")
    print("[2] Convert Money")
    print()
    print("'Press Any Key to Exit'")
    print()

def display_currencies(currencies):
    print("Available Currencies: " + ", ".join(currencies))
