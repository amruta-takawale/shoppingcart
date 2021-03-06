#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../shoppingcart/')
# import cart
# from lib.price_fetcher import PriceFetcher
import unittest
from shoppingcart.cart import ShoppingCart

class Testcart(unittest.TestCase):

    # Test item is present in the receipt
    def test_correct_value_present(self):
        cart = ShoppingCart('db')
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()
        self.assertEqual(receipt[0], "apple - 1 - €1.00")

    def test_returns_USD_currency(self):
        cart = ShoppingCart('db', 'USD')
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()
        self.assertEqual(receipt[0], "apple - 1 - US$1.16")

    #Total is present
    def test_item_total_is_present(self):
        cart = ShoppingCart('json')
        cart.add_item("apple", 1)
        cart.add_item("kiwi", 2)
        cart.add_item("pineapple", 9)

        receipt = cart.print_receipt()
        self.assertEqual(str(receipt[2]), 'Total - €3.24')

    #Total is present in UDS
    def test_item_total_is_present_in_USD(self):
        cart = ShoppingCart('db', 'USD')
        cart.add_item("apple", 1)
        cart.add_item("kiwi", 2)
        cart.add_item("pineapple", 9)

        receipt = cart.print_receipt()
        self.assertEqual(str(receipt[2]), 'Total - US$3.77')

    def test_add_item_with_multiple_quantity(self):
        cart = ShoppingCart('db')
        cart.add_item("apple", 2)
        cart.add_item("apple", 7)
        receipt = cart.print_receipt()

        assert receipt[0] == "apple - 9 - €9.00"


    def test_add_different_items(self):
        cart = ShoppingCart('db')
        cart.add_item("orange", 1)
        cart.add_item("kiwi", 1)

        receipt = cart.print_receipt()
        assert receipt[0] == "orange - 1 - €2.00"
        assert receipt[1] == "kiwi - 1 - €1.12"

if __name__ == '__main__':
    unittest.main()
