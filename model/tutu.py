import sys
import threading
import time
from random import randint

class Tutu(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(Tutu, self).__init__()
        self._stopper = threading.Event()

    def run(self):
        while(True):
            if randint(0,3) == 1:
                self.stopit()

            print('a')

    def stopit(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()
