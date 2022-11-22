import time

class FooBar:
    def __init__(self, n):
        self.n = n
        self.curr = 1


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while self.curr!=1:
                time.sleep(0.001)
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.curr=2


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while self.curr!=2:
                time.sleep(0.001)
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.curr=1