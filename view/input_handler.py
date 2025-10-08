def get_menu_option():
    return input("Option: ")

def get_conversion_input(validate_currency, validate_amount):
    source_currency = input("Source Currency: ").upper()
    validate_currency(source_currency)
    
    target_currency = input("Target Currency: ").upper()
    validate_currency(target_currency)     
    
    try:
        amount = float(input("Amount: ").replace(',', ''))
    except ValueError:
        raise ValueError("Please enter a valid amount.")
    
    validate_amount(amount)
     
    return source_currency, target_currency, amount

    
