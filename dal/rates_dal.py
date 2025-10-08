from utils.util import read_json_as_dict
from dal.abstract_rates import RatesABC

class RatesJsonDao(RatesABC):
    
    def retrieve_rates(self):
        return read_json_as_dict("rates.json")
    
    def search_rates(self, source_currency, target_currency):

        for rate in self.retrieve_rates():
            if ((rate["source_currency"] == source_currency and rate["target_currency"] == target_currency) or 
                (rate["source_currency"] == target_currency and rate["target_currency"] == source_currency)):
                return rate
        
        raise ValueError(f"No rate found for {source_currency} and {target_currency}")
    
    def retrieve_currencies(self):
        currencies = set()
        for rate in self.retrieve_rates():
            currencies.add(rate["source_currency"])
            currencies.add(rate["target_currency"])
        return sorted(list(currencies))
    
