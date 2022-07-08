from datetime import date

from stock_alerter.time_serie import TimeSerie
from exceptions import NotEnoughDataException


class MovingAvarage:

    def __init__(self, serie: TimeSerie, timespan: int) -> None:
        self.serie = serie
        self.timespan = timespan

    def value_on(self, end_date: date):
        moving_avarage_range = self.serie.get_closing_price_list(
            end_date, self.timespan)
         
        if len(moving_avarage_range) < self.timespan:
            raise NotEnoughDataException("Not enougth data")

        price_list = [item.value for item in moving_avarage_range]

        return sum(price_list)/len(price_list)
