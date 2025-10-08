import sys
from utils.util import format_value
from dal.rates_factory import RatesFactory

class RatesBll:
    
    def __init__(self, source):
        self.__rates__dao = RatesFactory().create_instance(source)
    
    def retrieve_rates(self):
        return self.__rates__dao.retrieve_rates()
    
    def convert_currency(self, source_currency, target_currency, amount):
         rates_data = self.__rates__dao.search_rates(source_currency, target_currency)
         return format_value((amount * rates_data["source_rate"]) / rates_data["target_rate"])
    
    def retrieve_currencies(self):
        return self.__rates__dao.retrieve_currencies()
    
    def validate_currency(self, currency):
        if currency not in self.__rates__dao.retrieve_currencies():
            raise ValueError("INVALID Currency")
    
    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if amount > sys.maxsize:
            raise ValueError("Amount too large.")
       

    


    