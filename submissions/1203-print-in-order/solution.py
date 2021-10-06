class Foo:
    def __init__(self):
        self.curr = 1


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.curr = 2


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.curr < 2:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.curr = 3


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.curr < 3:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
