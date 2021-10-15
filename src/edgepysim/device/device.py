import string
import abc

from ..application import Microservice
from ..resource import Resource


class Device(object):

    def __init__(self, resources: set[Resource]):
        self.resources = resources

    @abc.abstractmethod
    def get_resources_information(self) -> set[Resource]:
        pass

    @abc.abstractmethod
    def transfer_image(self) -> bool:
        pass

    @abc.abstractmethod
    def deploy_microservice(self, microservice: Microservice) -> string:
        pass

    @abc.abstractmethod
    def terminate_microservice(self, microservice_handler: string) -> bool:
        pass


class EdgeDevice(Device):

    def __init__(self, position: tuple[float, float], resources: set[Resource]):
        super().__init__(resources)
        self.position = position

    def get_position(self) -> tuple[float, float]:
        return self.position

    def deploy_microservice(self, microservice: Microservice):
        # check if image already available on the current machine

        # transfer the image

        # allocate resources
        pass


class CloudDevice(Device):

    def __init__(self, rack: string, resources: set[Resource]):
        super().__init__(resources)
        self.rack = rack

    def get_rack(self) -> string:
        return self.rack
