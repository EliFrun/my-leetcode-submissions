class Foo:
    def __init__(self):
        self.state = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:  
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.state = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.state < 1:
            time.sleep(0.001)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.state = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        while self.state < 2:
            time.sleep(0.001)
        printThird()

