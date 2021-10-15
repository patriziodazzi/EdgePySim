import string

from edgepysim.resource.requirement import ResourceRequirement


class Volume(object):
    def __init__(self, name: string, size: int):
        self.name = name
        self.size = size


class Image(object):

    def __init__(self, name: string, size: int):
        self.name = name
        self.size = size


class Microservice(object):

    def __init__(self, name: string, requirements: set[ResourceRequirement], image: Image, has_volumes=False,
                 volumes: set[Volume] = None, batch=False, length: int = -1):
        # Mandatory arguments (name, requirement, image)
        self.requirements = requirements
        self.name = name
        self.image = image

        # References to volumes (if any)
        if volumes is None: volumes = {}
        assert has_volumes == (len(volumes) > 0), "Error in the setting of Microservice volumes"
        self.has_volumes = has_volumes
        self.volumes = volumes

        # Information about length (if batch)
        assert batch == (length > 0), "Error in the setting of Microservice length"
        self.batch = batch
        self.length = length

    def get_name(self) -> string:
        return self.name

    def get_requirements(self) -> set[ResourceRequirement]:
        return self.requirements

    def get_image(self) -> Image:
        return self.image

    def has_volumes(self) -> bool:
        return self.has_volumes

    def get_volumes(self) -> set[Volume]:
        return self.volumes

    def is_batch(self) -> bool:
        return self.batch

    def length(self) -> int:
        return self.length


class Application(object):
    def __init__(self, name: string, components: set[Microservice]):
        self.components = components
        self.name = name

    def get_components(self) -> set[Microservice]:
        return self.components

    def get_name(self) -> string:
        return self.name
