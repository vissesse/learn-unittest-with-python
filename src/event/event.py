
class Event:
    def __init__(self) -> None:
        self.listeners = []

    def connect(self, listeners):
        self.listeners.append(listeners)

    def fire(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)
