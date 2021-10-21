import string

# from edgepysim.application.application import Microservice
# from edgepysim.application.application import Image
# from edgepysim.resource.resource import Resource
# from edgepysim.resource.resource import ResourceType
from edgepysim import *


class Device(object):

    def __init__(self, resources: dict[ResourceType, ResourceDescriptor]):
        self.resources = resources
        self.images: dict[string, Image] = {}
        self.microservices: dict[string, Microservice] = {}

    # private service methods
    def __enough_space_for_the_image__(self, size) -> bool:
        space = int(self.resources[ResourceType.STORAGE].get_value())
        if space > size:
            return True
        else:
            return False

    def __allocate_image__(self, img):
        new_space = int(self.resources[ResourceType.AVAILABLE_STORAGE].get_value()) - img.size
        self.resources[ResourceType.AVAILABLE_STORAGE].set_value(str(new_space))

    def __enough_resources_for_the_microservice__(self, microservice):
        satisfied = True
        for req in microservice.get_requirements():
            satisfied = satisfied and req.is_satisfied(self.resources)

    def __create_and_start_microservice__(self, microservice):
        self.__reduce_resources_availability__(microservice)

    def __free_microservice_resources__(self, param):
        pass

    # public methods
    def resources(self) -> dict[ResourceType, ResourceDescriptor]:
        return self.resources

    def is_image_available(self, name: string) -> bool:
        return name in self.images

    def get_image(self, name: string) -> Image:
        return self.images[name]

    def store_image(self, img: Image) -> bool:
        if self.__enough_space_for_the_image__(img.size):
            self.__allocate_image__(img)
            return True
        return False

    def get_microservice(self, microservice: Microservice) -> dict[string, Microservice]:
        output: dict[string, Microservice] = {}
        for ms_id, ms in self.microservices.items():
            if ms.get_name() == microservice.get_name():
                output[ms_id] = ms
        return output

    def has_microservice(self, microservice: Microservice) -> bool:
        for ms in self.microservices.values():
            if ms.get_name() == microservice.get_name():
                return True

        return False

    def start_microservice(self, microservice: Microservice) -> string:
        # check if image already available on the current machine
        if microservice.image not in self.images:
            return None

        # check if there are enough resources available on the device
        if not self.__enough_resources_for_the_microservice__(microservice):
            return None
        else:
            return self.__create_and_start_microservice__(microservice)

    def terminate_microservice(self, microservice_handler: string) -> bool:
        # note: we must check the ms is the last
        # one to unpin image
        if microservice_handler in self.microservices:
            self.__free_microservice_resources__(self.microservices[microservice_handler])
            del self.microservices[microservice_handler]
            return True
        return False


class EdgeDevice(Device):

    def __init__(self, position: tuple[float, float], resources: dict[ResourceType, ResourceDescriptor]):
        super().__init__(resources)
        self.position = position

    def get_position(self) -> tuple[float, float]:
        return self.position


class CloudDevice(Device):

    def __init__(self, rack: string, resources: dict[ResourceType, ResourceDescriptor]):
        super().__init__(resources)
        self.rack = rack

    def get_rack(self) -> string:
        return self.rack
