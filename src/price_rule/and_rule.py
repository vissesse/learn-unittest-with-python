

from stock_alerter.stock import Stock


class AndRule:

    def __init__(self, *args) -> None:
        self.rules = args

    def matches(self, exchange: dict[str, Stock]):
        return all([rule.matches(exchange) for rule in self.rules])
