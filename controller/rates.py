from bll.rates_bll import RatesBll

class Rates():
    
    def __init__(self, source):
        self.rates_bll = RatesBll(source) 

    def display_rates(self):
        print("\nSource Currency\t\tTarget Currency\t\tRate")
        for rate in self.rates_bll.retrieve_rates().get("rates", []):
            if rate['currency'] != "PHP":    
                print(f"     {rate['currency']}\t\t      PHP\t\t{rate['rate']}")

    def convert_rates(self, source_currency, target_currency, amount):
        print(f"\nConverted Amount:  {self.rates_bll.convert_currency(source_currency, target_currency, amount)} {target_currency}")

    def retrieve_currencies(self):
        return self.rates_bll.retrieve_currencies()
    
    def validate_currency(self, currency):
        return self.rates_bll.validate_currency(currency)
    
    def validate_amount(self, amount):
        return self.rates_bll.validate_amount(amount)