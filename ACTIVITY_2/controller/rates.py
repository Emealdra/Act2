from bll.rates_bll import RatesBll

class Rates():
    
    def __init__(self):
        self.rates_bll = RatesBll() 

    def display_rates(self):
        print("Source Ccy\t\tTarget Ccy\t\tRate")
        for rate in self.rates_bll.retrieve_rates().get("rates", []):
            if rate['currency'] != "PHP":    
                print(f"{rate['currency']}\t\t\tPHP\t\t\t{rate['rate']}")

    def convert_rates(self, source_currency, target_currency, amount):
        print(f"Converted Amount:  {self.rates_bll.convert_currency(source_currency, target_currency, amount)} {target_currency}")
