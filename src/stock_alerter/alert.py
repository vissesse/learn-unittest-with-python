

from price_rule.price_rule import PriceRule
from stock_alerter.stock import Stock


class Alert:
    """
    Maps a rule to an action, an trigger the action if de rule matches on any stock update
    """

    def __init__(self, descriction, rule: PriceRule, action) -> None:
        self.descriction = descriction
        self.rule = rule
        self.action = action

    def connect(self, exchange: dict[str, Stock]):
        self.exchange = exchange
        dependent_stocks = self.rule.depends_on()
        for stock in dependent_stocks:
            exchange[stock].updated.connect(self.check_rule())

    def check_rule(self):
        if self.rule.matches(self.exchange):
            self.action.execute(self.descriction)
