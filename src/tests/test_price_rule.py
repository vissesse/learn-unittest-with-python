from datetime import date
import unittest


from stock_alerter.stock import Stock
from price_rule.price_rule import PriceRule


class PriceRuleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        goog = Stock("GOOG")
        goog.price_update(timestamp=date(2022, 4, 11), price=11)
        cls.exchange = {'GOOG': goog}

    def test_PriceRule_match(self):
        """ PriceRule match when it meet de condictions"""
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        self.assertTrue(rule.matches(self.exchange),
                        'match  must be true or exists simbol')

    def test_PriceRule_is_false(self):
        """Price rule is false if the stocke is not in exchange"""

        rule = PriceRule("MST", lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_PriceRule_update_false(self):
        """ PriceRule is false in has not an update yet"""
        self.exchange['AAPL'] = Stock("AAPL")

        rule = PriceRule("AAPL", lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_PriceRule_only_depends_on_its_stock(self):
        """"""
        rule = PriceRule("MFST", lambda stock: stock.price > 10)
        self.assertEqual({"MFST"}, rule.depends_on())
