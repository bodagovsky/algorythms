from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.router = {
            0:self.first,
            1:self.second,
            2:self.third,
            3:self.fourth,
            4:self.fifth
        }
        
        self.f_first = Lock()
        self.f_sec = Lock()
        self.f_third = Lock()
        self.f_fourth = Lock()
        self.f_fifth = Lock()
    

    # call the functions directly to execute, for example, eat()
    def first(self,pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]'):
        self.f_first.acquire()
        self.f_fifth.acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.f_first.release()
        self.f_fifth.release()
    
    def second(self,pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]'):
        self.f_first.acquire()
        self.f_sec.acquire()
        pickRightFork()
        pickLeftFork()
        eat()
        putLeftFork()
        putRightFork()
        self.f_first.release()
        self.f_sec.release()
    
    def third(self,pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]'):
        self.f_third.acquire()
        self.f_sec.acquire()
        pickRightFork()
        pickLeftFork()
        eat()
        putLeftFork()
        putRightFork()
        self.f_third.release()
        self.f_sec.release()
    
    def fourth(self,pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]'):
        self.f_third.acquire()
        self.f_fourth.acquire()
        pickRightFork()
        pickLeftFork()
        eat()
        putLeftFork()
        putRightFork()
        self.f_third.release()
        self.f_fourth.release()
    
    def fifth(self,pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]'):
        self.f_fourth.acquire()
        self.f_fifth.acquire()
        pickRightFork()
        pickLeftFork()
        eat()
        putLeftFork()
        putRightFork()
        self.f_fourth.release()
        self.f_fifth.release()
    
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        self.router[philosopher](pickLeftFork,
                                pickRightFork,
                                eat,
                                putLeftFork,
                                putRightFork)
