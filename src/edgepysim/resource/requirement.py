import abc
import string

# from edgepysim.device.device import Device
# from edgepysim.resource.resource import ResourceDescriptor, ResourceType  # ,IntegerResourceDescriptor

from edgepysim import *


class Requirement(abc.ABC):

    def __init__(self, rd: ResourceDescriptor, matching_rule):
        self.rd = rd
        self.matching_rule = matching_rule

    @abc.abstractmethod
    def __matching_rule__(self):
        pass

    def is_satisfied_by_resource(self, actual_resource: ResourceDescriptor) -> bool:

        if self.__matching_rule__() == "eq":
            return actual_resource == self.rd
        elif self.__matching_rule__() == "gt":
            return actual_resource > self.rd
        elif self.__matching_rule__() == "lt":
            return actual_resource < self.rd
        elif self.__matching_rule__() == "ge":
            return actual_resource >= self.rd
        elif self.__matching_rule__() == "le":
            return actual_resource <= self.rd

        return False

    def is_satisfied_by_device(self, dev: Device) -> bool:

        available_resources = dev.resources()

        actual_resource = None
        for i_rt, i_rd in available_resources.items():
            if i_rt == self.rd.res_type:
                actual_resource = i_rd

        if not actual_resource:
            return False

        if self.__matching_rule__() == "eq":
            return actual_resource == self.rd
        elif self.__matching_rule__() == "gt":
            return actual_resource > self.rd
        elif self.__matching_rule__() == "lt":
            return actual_resource < self.rd
        elif self.__matching_rule__() == "ge":
            return actual_resource >= self.rd
        elif self.__matching_rule__() == "le":
            return actual_resource <= self.rd

        return False


class GenericIntegerRequirement(Requirement):

    def __init__(self, rd: ResourceDescriptor, matching: string):
        #        IntegerResourceDescriptor.__init__(self, res_type, res_value, matching)
        super().__init__(rd, matching)
        self.matching = matching

    def __matching_rule__(self):
        return self.matching


class NetworkBandwidthRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(ResourceDescriptor(ResourceType.NETWORK_BANDWIDTH, res_value), matching="ge")


class StorageSpaceRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(ResourceDescriptor(ResourceType.STORAGE, res_value), matching="ge")


class MemoryAmountRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(ResourceDescriptor(ResourceType.MEMORY_AMOUNT, res_value), matching="ge")


class ProcessingCapacityResourceRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(ResourceDescriptor(ResourceType.COMPUTING_CAPACITY, res_value), matching="ge")
