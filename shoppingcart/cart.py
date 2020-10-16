import typing
import collections

from lib.price_fetcher import get_price

from . import abc


class ShoppingCart(abc.ShoppingCart):
    def __init__(self, source: str):
        self._items = collections.OrderedDict()
        self._price_source = source

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
            if price != 0.0:

                total = total + price
                price_string = "€%.2f" % price

                lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)
                

        lines.append("Total - " + "€" + str(total))
        return lines

    def _get_product_price(self, product_code: str) -> float:
        price = 0.0
        product = get_price(self._price_source, product_code)
        if product:
            price = product['price']
        return price
