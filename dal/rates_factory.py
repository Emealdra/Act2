from dal.rates_dal import RatesJsonDao

class RatesFactory:

    def create_instance(self, source):

        source_map  = {
            "json":  RatesJsonDao,
            "db":    RatesJsonDao,
            "api": RatesJsonDao
        }

        source = source_map.get(source, None)

        if source == None:
            raise Exception("Invalid data source")

        return source()
        