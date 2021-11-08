from __future__ import annotations
import string

#from simulator1edge.device.base import Device
#from simulator1edge.resource.descriptor import ResourceDescriptor, NetworkBandwidthResourceDescriptor

from simulator1edge.core import *


class EdgeDevice(Device):

    def __init__(self, position: tuple[float, float], resources: list[ResourceDescriptor]):
        super().__init__(resources)
        self._position = position

    def __str__(self):
        return super().__str__()

    @property
    def position(self) -> tuple[float, float]:
        return self._position

    @position.setter
    def position(self, value: tuple[float, float]):
        self._position = value


class CloudDevice(Device):

    def __init__(self, availability_zone: string, resources: list[ResourceDescriptor]):
        super().__init__(resources)
        self._availability_zone = availability_zone

    def __str__(self):
        return super().__str__()

    @property
    def availability_zone(self) -> string:
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, value: string):
        self._availability_zone = value


class NetworkSwitchRouter(Device):

    def __init__(self, bandwidth=1000):
        resources = [NetworkBandwidthResourceDescriptor(str(bandwidth))]
        super().__init__(resources)
