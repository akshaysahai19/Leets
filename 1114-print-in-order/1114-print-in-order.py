import threading

class Foo:
    def __init__(self):
        self.done = 1
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done = 2


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.done!=2:
            # block for a moment
            time.sleep(0.01)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.done = 3


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.done!=3:
            # block for a moment
            time.sleep(0.01)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.done = 0