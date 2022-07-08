from typing import Any


class Mock:

    def __init__(self) -> None:
        self.called = False
        self.params = ()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.called = True
        self.params = (args, kwds)
