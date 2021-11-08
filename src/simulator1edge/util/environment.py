import random
import simpy


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Simulation(object, metaclass=Singleton):

    def __init__(self, time: int = 100, seed: int = 42):
        random.seed(seed)
        self._env = simpy.Environment()
        self._time = time

    @property
    def env(self):
        return self._env

    @property
    def time(self):
        return self._time

    def run(self):
        self.env.run(until=self.time)
