from enum import Enum


class ResourceType(Enum):
    STORAGE = 1
    MEMORY_AMOUNT = 2
    COMPUTING_CAPACITY = 3
    NETWORK_BANDWIDTH = 4
    FPGA = 5
    GPU = 6
    WIFI = 7
    GPS = 8
    RACK = 9


class Orchestrator(object):
    def __init__(self):
        pass