from datetime import date
import unittest

from stock_alerter.time_serie import TimeSerie


class TimeSerieTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.times_serie = TimeSerie()
        cls.times_serie.update(date(2020, 1, 2), 10.2)
        cls.times_serie.update(date(2020, 3, 2), 11.2)
        cls.times_serie.update(date(2020, 2, 2), 9.2)

    def test_closing_price_list(self):
        data = date(2020, 2, 2)
        closing_list = self.times_serie.get_closing_price_list(data, 5)
        self.assertIsNotNone(closing_list, "List mast be None")

    def test_timeseSerie_update_price(self):
        self.times_serie.update(date(2022, 6, 3), 20.33)
        self.assertIn((date(2022, 6, 3), 20.33), self.times_serie.series, 'Erro ao acualizar')
