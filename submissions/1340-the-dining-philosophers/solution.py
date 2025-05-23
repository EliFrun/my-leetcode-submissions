class DiningPhilosophers:
    locks = [False] * 5
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   n: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        while DiningPhilosophers.locks[(5 + n - 1) % 5] or DiningPhilosophers.locks[(5 + n + 1) % 5]:
            sleep(0.0013)
        DiningPhilosophers.locks[n] = True
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        DiningPhilosophers.locks[n] = False
        
        
