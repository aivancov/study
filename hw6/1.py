from itertools import cycle
from time import sleep

MODES = {
    '1Red': 7, '2Yellow': 2, '3Green': 4, '4Yellow': 2}
class TrafficLight:
    def __init__(self):
        self.__color = None
        self.repeat = 15

    def running(self):
        count = 0
        for color in cycle(MODES.keys()):
            if count >=  self.repeat:
                break
            self.__color = color[1:]
            print(self.__color)
            sleep(MODES[color])
            count += 1


tl = TrafficLight()
tl.running()
