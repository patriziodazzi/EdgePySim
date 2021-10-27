import string
from abc import ABC, abstractmethod
from typing import Any

from edgepysim.device.base import Device, CloudDevice
from edgepysim.resource.descriptor import ResourceDescriptor


class DeviceFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_devices(self, description: list[(list[ResourceDescriptor], int)], features: dict[string, Any]) \
            -> list[Device]:
        pass


class CloudDeviceFactory(DeviceFactory):

    def __init__(self):
        pass

    def create_devices(self, description: list[(list[ResourceDescriptor], int)], features: dict[string, Any]) -> list[Device]:

        cloud_name = "generic_cloud"
        if features['cloud_name']:
            cloud_name = features['cloud_name']

        devices: list[CloudDevice] = []
        for device_template, device_cardinality in description:
            for i in range(device_cardinality):
                devices.append(CloudDevice(cloud_name, device_template))

        return devices
