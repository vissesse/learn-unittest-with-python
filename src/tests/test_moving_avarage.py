from datetime import date
from os import times
import unittest

from stock_alerter.moving_avarage import MovingAvarage
from stock_alerter.time_serie import TimeSerie


class MovingAvarageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.time_serie = TimeSerie()
        cls.time_serie.update(date(2022, 7, 4), 1.27)
        cls.time_serie.update(date(2022, 5, 3), 5.27)
        cls.time_serie.update(date(2022, 4, 23), 5.27)
        cls.time_serie.update(date(2022, 6, 3), 3.27)

    def test_MovingAvarage_value_on(self):
        ma = MovingAvarage(self.time_serie, 5)

        self.assertAlmostEqual(
            3.27, ma.value_on(date(2022, 7, 3)), delta=1, msg="soma invalida"
        )
