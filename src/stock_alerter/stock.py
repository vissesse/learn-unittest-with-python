from datetime import date, timedelta

from stock_alerter import TimeSerie
from stock_alerter import MovingAvarage
from utils import StockSignal
from exceptions import NotEnoughDataException


class Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5

    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.history = TimeSerie()

    def price_update(self, timestamp: date, price: float):
        if price < 0:
            raise ValueError("Preço nao pode ser negativo!")
        
        self.history.update(timestamp, price)

    @property
    def price(self):
        try:
            return self.history[-1].value
        except IndexError:
            return None

    @property
    def data(self):
        return self.history[-1].data if self.history else None

    def is_increasing_trend(self) -> bool:
        """ Verdade caso o preco Subir 3 vezes"""
        return self.history[-3].value < self.history[-2].value < self.history[-1].value

    def get_crossover_signal(self, on_date):
        long_term_ma = MovingAvarage(self.history, self.LONG_TERM_TIMESPAN)
        short_term_ma = MovingAvarage(self.history, self.SHORT_TERM_TIMESPAN)
        
        try:
            if self.is_crossover_below_to_above(on_date, short_term_ma, long_term_ma):
                return StockSignal.BUY.value

            if self.is_crossover_below_to_above(on_date, long_term_ma, short_term_ma):
                return StockSignal.SELL.value

        except NotEnoughDataException:
            return StockSignal.NEUTRAL.value
        
        return StockSignal.NEUTRAL.value 
    
 
    def is_crossover_below_to_above(self, on_date, ma: MovingAvarage, reference_ma: MovingAvarage):
        prev_date = on_date - timedelta(1)
        return ma.value_on(prev_date) < reference_ma.value_on(prev_date) and ma.value_on(on_date) > reference_ma.value_on(on_date)