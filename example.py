from visual_logging import VisualLogger
from time import sleep
from random import random

logger = VisualLogger(online=True, file='tracing.log')


@logger.logit
def some_function(a, b, c):
    return a + b + c


@logger.logit
class Tree:
    a = 1

    def method1(self, attr):
        return attr + 1

    def method2(self, sleep_time):
        sleep(sleep_time)
        return sleep_time

    def method3(self):
        return random()

    def method4(self):
        return 'sadfjsofjsdijfodsjgasjfsadf'

    def rec(self, value):
        sleep(0.5)
        if random() < 0.8:
            self.method3()
        if random() < 0.1:
            self.rec(2)
        if value > 0:
            self.rec(value - 1)


if __name__ == '__main__':
    for i in range(4):
        print(some_function(i, i + 1, i + 2))

    t = Tree()
    t.method1(5)
    t.method3()
    t.method2(1.24)
    t.rec(3)
    t.method2(1.24)
    t.method4()
    t.rec(3)
    t.method1(5)
    t.rec(4)
    # print(logger.calls())
