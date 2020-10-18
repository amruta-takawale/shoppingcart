import typing
import collections
from currency_converter import CurrencyConverter

from lib.price_fetcher import get_price

from . import abc

class ShoppingCart(abc.ShoppingCart):
    def __init__(self, source: str, currency='EUR'):
        #insert items based on order in which item being added
        self._items = collections.OrderedDict()
        self._price_source = source
        self._currency = currency

    def add_item(self, product_code: str, quantity: int):
        if quantity > 0:
            if product_code not in self._items:
                self._items[product_code] = quantity
            else:
                q = self._items[product_code]
                self._items[product_code] = q + quantity
        else:
            print("Please add quantity greater than 0")

    def print_receipt(self) -> typing.List[str]:
        lines = []
        total = 0.0

        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]
            #Do not add item to receipt if price is zero
            if price != 0.0:
                total = total + price
                price_string = "%.2f" % price

                lines.append(item[0] + " - " + str(item[1]) + ' - ' + self._get_currency_symbol() + price_string)
                

        lines.append("Total - " + self._get_currency_symbol() + "%.2f" % total)
        return lines

    #Fetched prices from db or json file and converts price to supported currency
    def _get_product_price(self, product_code: str) -> float:
        price = 0.0
        product = get_price(self._price_source, product_code)
        #Check product is present in db or json file and return price
        if product:
            price = product['price']
            if self._currency != 'EUR':
                price = CurrencyConverter().convert(product['price'], 'EUR' ,self._currency)

        return price

    #Get currency symbol
    def _get_currency_symbol(self):
        currency = self._currency
        if currency == 'EUR':
            return '€'
        elif currency == 'USD':
            return 'US$'
        elif currency == 'JPY':
            return '¥'
        elif currency == 'GBP':
            return '£'

