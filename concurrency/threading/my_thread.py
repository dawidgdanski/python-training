import time
from threading import Thread


class MyThread(Thread):

    def __init__(self, name, delay):
        Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting thread %s.' % self.name)
        _thread_count_down(self.name, self.delay)
        print('Finished thread %s.' % self.name)


def _thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print('Thread %s counting down: %i...' % (name, counter))
        counter -= 1
