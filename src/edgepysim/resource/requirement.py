import abc
import string

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

    def is_satisfied_by_device(self, dev) -> bool:

        available_resources = dev.get_resources()

        actual_resource = None
        for i_rt, i_rd in available_resources.items():
            if i_rt == self.rd.res_type:
                actual_resource = i_rd

        if not actual_resource:
            return False

        return self.is_satisfied_by_resource(actual_resource)


class RequirementSet(object):

    def __init__(self, reqs: set[Requirement]):
        self.requirement_set = reqs

    def are_satisfied_by_device(self, dev) -> bool:
        return all(map(lambda r: r.is_satisfied_by_device(dev), self.requirement_set))


class GenericIntegerRequirement(Requirement):

    def __init__(self, rd: ResourceDescriptor, matching: string):
        super().__init__(rd, matching)
        self.matching = matching

    def __matching_rule__(self):
        return self.matching


class NetworkBandwidthRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(IntegerResourceDescriptor(ResourceType.NETWORK_BANDWIDTH, res_value), matching="ge")


class StorageSpaceRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(IntegerResourceDescriptor(ResourceType.STORAGE, res_value), matching="ge")


class MemoryAmountRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(IntegerResourceDescriptor(ResourceType.MEMORY_AMOUNT, res_value), matching="ge")


class ProcessingCapacityResourceRequirement(GenericIntegerRequirement):
    def __init__(self, res_value: string):
        super().__init__(IntegerResourceDescriptor(ResourceType.COMPUTING_CAPACITY, res_value), matching="ge")
