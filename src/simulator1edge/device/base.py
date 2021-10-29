import copy
import string

from simulator1edge.application.base import Image, Microservice
from simulator1edge.resource.descriptor import ResourceDescriptor, ResourceType


class Device(object):
    _num_of_devices: int = 0

    def __init__(self, resources: list[ResourceDescriptor]):
        Device._num_of_devices += 1
        self._name = str("device." + str(Device._num_of_devices))
        self._resources: dict[ResourceType, ResourceDescriptor] = {copy.deepcopy(res.type): copy.deepcopy(res) for res in resources}

        self._images: dict[string, Image] = {}
        self.microservices: dict[string, Microservice] = {}

    def __str__(self):
        return self.name

    # private service methods
    def _enough_space_for_the_image(self, size) -> bool:
        space = int(self.resources[ResourceType.STORAGE].value)
        if space > size:
            return True
        else:
            return False

    def _allocate_image(self, img):
        new_space = int(self.resources[ResourceType.STORAGE].value) - img.size
        self.resources[ResourceType.STORAGE].value = (str(new_space))

    def _enough_resources_for_the_microservice(self, microservice) -> bool:
        satisfied = True
        for req in microservice.requirements:
            satisfied = satisfied and req.is_satisfied_by_resource(self.resources.get(req.resource_type))
        return satisfied

    def _create_and_start_microservice(self, microservice):
        self._reduce_resources_availability(microservice)

    # TODO: provide implementation
    def _free_microservice_resources(self, param):
        pass

    # public properties
    @property
    def name(self):
        return self._name

    @property
    def resources(self) -> dict[ResourceType, ResourceDescriptor]:
        return self._resources

    @resources.setter
    def resources(self, value: dict[ResourceType, ResourceDescriptor]):
        self._resources = value

    @property
    def images(self):
        return self._images

    def is_image_available(self, name: string) -> bool:
        return name in self.images

    def get_image_with_name(self, name: string) -> Image:
        return self.images[name]

    # TODO check if image is already stored
    def store_image(self, img: Image) -> bool:
        if self._enough_space_for_the_image(img.size):
            self._allocate_image(img)
            self.images[img.name] = img
            return True
        return False

    def get_microservice(self, microservice: Microservice) -> dict[string, Microservice]:
        output: dict[string, Microservice] = {}
        for ms_id, ms in self.microservices.items():
            if ms.name == microservice.name:
                output[ms_id] = ms
        return output

    def has_microservice(self, microservice: Microservice) -> bool:
        for ms in self.microservices.values():
            if ms.name == microservice.name:
                return True

        return False

    def start_microservice(self, microservice: Microservice) -> string:
        # check if image already available on the current machine
        if microservice.image.name not in self.images:
            return None

        # check if there are enough resources available on the device
        if not self._enough_resources_for_the_microservice(microservice):
            return None
        else:
            self._create_and_start_microservice(microservice)

        # store microservice handle in the internal data structure
        self.microservices[microservice.id] = microservice

    def terminate_microservice(self, microservice_handler: string) -> bool:
        # TODO: we must check the ms is the last one to unpin image
        if microservice_handler in self.microservices:
            self._free_microservice_resources(self.microservices[microservice_handler])
            del self.microservices[microservice_handler]
            return True
        return False

    def _reduce_resources_availability(self, microservice):
        if self._enough_resources_for_the_microservice(microservice):
            for req in microservice.requirements:
                resource_availability = self.resources[req.resource_type]
                resource_availability -= req.rd
                self.resources[req.resource_type] = resource_availability
