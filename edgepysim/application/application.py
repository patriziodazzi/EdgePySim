import string

from edgepysim.resource import ResourceRequirement


class Microservice(object):

    def __init__(self, name: string, requirements: set[ResourceRequirement], length: int = -1, batch=False):
        self.requirements = requirements
        self.batch = batch
        self.name = name
        self.length = length
        assert batch == (length > 0), "Error in the setting of Microservice"

    def get_requirements(self) -> set[ResourceRequirement]:
        return self.requirements

    def get_name(self) -> string:
        return self.name

    def is_batch(self) -> bool:
        return self.batch

    def get_length(self) -> int:
        return self.length


class Application(object):
    def __init__(self, name: string, components: set[Microservice]):
        self.components = components
        self.name = name

    def get_components(self) -> set[Microservice]:
        return self.components

    def get_name(self) -> string:
        return self.name
