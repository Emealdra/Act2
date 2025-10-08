from controller.rates import Rates
from view.menu import display_logo, display_options, display_currencies
from view.input_handler import get_menu_option, get_conversion_input

def main():
    
    rates = Rates("json")
   
    display_logo()

    while True:
        display_options()
        
        option = get_menu_option()
        if option == "1":
            rates.display_rates()
        elif option == "2":

            display_currencies(rates.retrieve_currencies())
            try:
                rates.convert_rates(*get_conversion_input(rates.validate_currency, rates.validate_amount))
            except Exception as e:
                print(str(e))
        else:
            break
main()
