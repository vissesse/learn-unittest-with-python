from datetime import date
import unittest
from unittest import mock

from stock_alerter.alert import Alert
from stock_alerter.stock import Stock
from price_rule.price_rule import PriceRule


class TestAction:

    executed = False

    def execute(self, descriction):
        self.execute = True


class AlertTest(unittest.TestCase):

    def test_is_executed_when_the_rule_match(self):
        exchange = {'GOOG': Stock("GOOG")}

        rule = mock.MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {'GOOG'}

        action = mock.MagicMock()  # TestAction()
        alert = Alert('simple alert', rule, action)
        alert.connect(exchange)

        exchange['GOOG'].price_update(date(2014, 2, 10), 11)
        action.execute.assert_called_with('simple alert')
