from types import FunctionType


from stock_alerter import Stock


class PriceRule:
    """
    Price rule são regras que disparadas quando o stocke de preco 
    satifaz um certa condição (usualemnte: mairo que, igual ou menor 
    que um preco dado )
    """

    def __init__(self, simbol: str, condiction: callable(FunctionType)) -> None:
        """_summary_

        Args:
            simbol (str): Simbol of the ruel
            condiction (callable): function or object collable
        """
        self.simbol = simbol
        self.condiction = condiction

    def matches(self, exchange: dict[str, Stock]):
        try:
            stock = exchange[self.simbol]
        except KeyError:
            return False
        return self.condiction(stock) if stock.price else False

    def depends_on(self):
        return {self.simbol}


