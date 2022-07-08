from datetime import date
import unittest

from stock_alerter.stock import Stock


class StockTest(unittest.TestCase):

    def setUp(self) -> None:
        self.goog = Stock("GOOG")

    def test_price_of_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stok_price_update(self):
        """Deve setar o preco e pela data expecificada"""
        self.goog.price_update(date(2022, 4, 6), price=10)
        self.assertEqual(self.goog.price, 10, 'Preco inesperado')

    def test_negative_price_should_throw_valueError(self):
        "Lancar excepção caso  data for negativa"
        goog = Stock("GOOG")
        # try:
        #    goog.price_update(date(2002, 4, 1), -3)
        # except ValueError:
        #    return
        # self.fail("Error")
        # self.assertRaises(
        #    ValueError, goog.price_update,
        #    date(2022, 4, 6), -2.2
        # )

        with self.assertRaises(ValueError):
            goog.price_update(date(2020, 4, 4), -1)

    def test_stock_price_should_give_the_latest_price(self):

        self.goog.price_update(date(2020, 4, 12), 10.01)
        self.goog.price_update(date(2020, 5, 11), 8.39)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.01)


class StockTrendTest(unittest.TestCase):
    def setUp(self) -> None:
        self.goog = Stock("Goog")

    def give_serie_of_prices(self, prices):

        dates = [date(2020, 2, 11), date(2020, 2, 12), date(2020, 2, 13)]
        for data, price in zip(dates, prices):
            self.goog.price_update(data, price)

    def test_price_increaseing_trend(self):
        """method: 'is_increasing_trend' será 'True' se  'price' incrementar por 3 updates"""
        prices = [8, 10, 12]
        self.give_serie_of_prices(prices)
        self.assertTrue(self.goog.is_increasing_trend())

    def test_price_decreases_trend(self):
        """metodo: 'is_increasing_trend' return False caso os preços drecrementem"""
        prices = [8, 12, 10]
        self.give_serie_of_prices(prices)
        self.assertFalse(self.goog.is_increasing_trend())

    def test_price_equal(self):
        """method: 'is_increasing_trend' será False caso houver precos inguais"""

        prices = [8, 10, 10]
        self.give_serie_of_prices(prices)
        self.assertFalse(self.goog.is_increasing_trend())

    def test_neutral_crossover_signal(self):
        self.goog.price_update(date(2020, 1, 10), 5.23)
        self.goog.price_update(date(2020, 1, 11), 2.10)
        self.goog.price_update(date(2020, 2, 12), 3.01)
        self.goog.price_update(date(2020, 2, 13), 6.02)
        self.goog.price_update(date(2020, 3, 14), 9.02)
        self.goog.price_update(date(2020, 3, 15), 1.10)
        signal = self.goog.get_crossover_signal(date(2020, 4, 11))
        self.assertEqual(signal, 0)
