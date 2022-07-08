import unittest
from datetime import date

from stock_alerter.stock import Stock
from price_rule.price_rule import PriceRule
from price_rule.and_rule import AndRule

class AndRuleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        goog = Stock("GOOG")
        goog.price_update(date(2014, 2, 11), 10)
        goog.price_update(date(2014, 1, 10), 8)
        goog.price_update(date(2014, 2, 12), 12)
        
        msft = Stock("MSFT")
        msft.price_update(date(2014, 2, 10), 10)
        msft.price_update(date(2014, 2, 11), 10)
        msft.price_update(date(2014, 2, 12), 12)
        
        redhat = Stock("RHT")
        redhat.price_update(date(2014, 2, 10), 7)
        
        cls.exchange = {"GOOG": goog, "MSFT": msft, "RHT": redhat}

    def test_match_rules_true(self):
        """ AndRule mutches if all components rules are true"""
        rule = AndRule(
            PriceRule('GOOG', lambda stock: stock.price > 8),
            PriceRule("MSFT", lambda stock: stock.price > 10)
        )
        
        self.assertTrue(rule.matches(self.exchange), 'Preço abaixo do esperado')
