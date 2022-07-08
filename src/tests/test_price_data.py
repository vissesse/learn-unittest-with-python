from datetime import date
import unittest

from stock_alerter.stock import Stock


class DatapriceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.goog = Stock("goog")
        #cls.exchange = {'good': goog}

    def test_update_must_have_an_date(self):
        "todo preco de deve  terdata"
        self.goog.price_update(date(2022, 4, 6), price=10)
        self.assertIsNotNone(self.goog.data, 'Data nao pode ser invalida')

    def test_data_should_give_the_latest(self):
        """Retornar ultima data mesmo se as actulizações forem feita desordenadamente"""
        self.goog.price_update(date(2024, 4, 6), price=8)
        self.goog.price_update(date(2023, 4, 6), price=10)
        self.assertEqual(self.goog.price, 8, "Deve retornar a ultima data")
