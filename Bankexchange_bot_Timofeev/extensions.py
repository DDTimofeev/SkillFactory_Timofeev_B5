import requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass

class Get_price:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        quote_ticker=keys[quote]
        base_ticker=keys[base]

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            quote_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать кол-во {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=BTH')
        total_base = json.loads(r.content)[keys[base]]*amount

        return total_base
