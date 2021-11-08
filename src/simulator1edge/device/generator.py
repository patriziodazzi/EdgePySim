from __future__ import annotations

import string
from abc import ABC, abstractmethod
from typing import Any

# from simulator1edge.device.base import Device
# from simulator1edge.resource.descriptor import ResourceDescriptor

from simulator1edge.core import *
from simulator1edge.device.concrete import CloudDevice


class DeviceFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_device_instances(self, features: dict[string, Any]) -> list[Device]:
        pass


class CloudDeviceFactory(DeviceFactory):

    CLD_NAM_FEAT = 'cloud_name'
    _STD_CLD_NAM_FEAT = 'generic_cloud'

    def __init__(self, description: list[(list[ResourceDescriptor], int)], features: dict[string, Any] = None):
        super().__init__()
        self._description = description

    @property
    def description(self) -> list[(list[ResourceDescriptor], int)]:
        return self._description

    @description.setter
    def description(self, description: list[(list[ResourceDescriptor], int)]):
        self._description = description

    def create_device_instances(self, features: dict[string, Any]) -> list[Device]:

        cloud_name = CloudDeviceFactory._STD_CLD_NAM_FEAT
        if features[CloudDeviceFactory.CLD_NAM_FEAT]:
            cloud_name = features[CloudDeviceFactory.CLD_NAM_FEAT]

        devices: list[Device] = []
        for device_template, device_cardinality in self.description:
            for i in range(device_cardinality):
                devices.append(CloudDevice(cloud_name, device_template))

        return devices
