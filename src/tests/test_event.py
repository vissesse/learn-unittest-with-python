import unittest
from unittest import mock

from event.event import Event


class EventTest(unittest.TestCase):

    def test_a_listen_is_notified_when_a_method_is_raised(self):
        listener = mock.Mock()
        event = Event()

        event.connect(listener)
        event.fire()

        self.assertTrue(listener.called, "Metodo não executado")

    def test_listener_is_passed_right_parameters(self):
        listener = mock.Mock()
        event = Event()

        event.connect(listener)
        # caso quera um parametro quaquer 'mock.Any'
        event.fire(5, funcao="teste")

        #listener.assert_called_with(5, funcao='teste')
        listener.assert_has_calls([mock.call(5, funcao='teste')])

    def test_listener_is_called_once(self):
        listener = mock.Mock()

        event = Event()

        event.connect(listener)
        event.fire(3, k=5) 

        listener.assert_called_once()

    def test_listener_is_colled_twace(self):
        listener = mock.Mock()
        event = Event()

        event.connect(listener)
        event.fire(3, 4, k=3)
        event.fire(2, 5)

        listener.assert_has_calls([mock.call(3, 4, k=3), mock.call(2, 5)])
