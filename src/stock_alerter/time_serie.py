from datetime import date, timedelta
import bisect

import collections

Update = collections.namedtuple("Update", ['data', 'value'])


class TimeSerie:

    def __init__(self) -> None:
        self.series = []

    def update(self, data: date, value: float):
        bisect.insort_left(self.series, Update(data, value))

    def __getitem__(self, index):
        return self.series[index]

    def get_closing_price_list(self, on_date: date, num_days: int) -> list[tuple[date, float]]:
        close_price_list = []
        for i in range(num_days):
            chk = on_date - timedelta(i)
            for price_event in reversed(self.series):
                if price_event.data > chk:
                    pass
                if price_event.data == chk:
                    close_price_list.insert(0, price_event)
                    break
                if price_event.data < chk:
                    close_price_list.insert(0, price_event)
                    break
        return close_price_list


