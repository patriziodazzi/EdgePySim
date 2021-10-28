import abc
import copy
import string
from enum import Enum


class ResourceType(str, Enum):
    STORAGE = 'storage'
    MEMORY_AMOUNT = 'memory_amount'
    COMPUTING_CAPACITY = 'computing_capacity'
    NETWORK_BANDWIDTH = 'network_bandwidth'
    FPGA = 'FPGA'
    GPU = 'GPU'
    WIFI = 'WIFI'
    GPS = 'GPS'
    AVAILABILITY_ZONE = 'availability_zone'


class ResourceDescriptor(abc.ABC):

    def __init__(self, res_type: ResourceType, res_value):
        self.type = res_type
        self.value = res_value

    def __str__(self):
        return str(self.type) + " : " + str(self.value)

    def __isub__(self, other):
        _sub: ResourceDescriptor = self - other
        # self.res_value = self.__sub__(other)
        self.value = _sub.value
        return self

    def __iadd__(self, other):
        _sum: ResourceDescriptor = self + other
        # self.res_value = self.__add__(other)
        self.value = _sum.value
        return self

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    @abc.abstractmethod
    def __gt__(self, other):
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __add__(self, other):
        pass

    @abc.abstractmethod
    def __sub__(self, other):
        pass

    @property
    def type(self) -> ResourceType:
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self) -> string:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class IntegerResourceDescriptor(ResourceDescriptor):

    def __init__(self, res_type: ResourceType, res_value: string):
        super().__init__(res_type, res_value)

    def __gt__(self, other):
        return int(self.value) > int(other.value)

    def __eq__(self, other):
        return int(other.value) == int(self.value)

    def __add__(self, other):
        ret: IntegerResourceDescriptor = copy.deepcopy(self)
        ret.value = (int(self.value) + int(other.value))
        return ret

    def __sub__(self, other):
        ret: IntegerResourceDescriptor = copy.deepcopy(self)
        ret.value = (int(self.value) - int(other.value))
        return ret


class MemoryAmountResourceDescriptor(IntegerResourceDescriptor):

    def __init__(self, res_value: string):
        super().__init__(ResourceType.MEMORY_AMOUNT, res_value)


class NetworkBandwidthResourceDescriptor(IntegerResourceDescriptor):

    def __init__(self, res_value: string):
        super().__init__(ResourceType.NETWORK_BANDWIDTH, res_value)


class ProcessingCapacityResourceDescriptor(IntegerResourceDescriptor):

    def __init__(self, res_value: string):
        super().__init__(ResourceType.COMPUTING_CAPACITY, res_value)


class StorageSpaceResourceDescriptor(IntegerResourceDescriptor):

    def __init__(self, res_value: string):
        super().__init__(ResourceType.STORAGE, res_value)
