from __future__ import annotations

import string

from simulator1edge.core import *

# from simulator1edge.resource.requirement import Requirement, StorageSpaceRequirement


class Volume(object):
    def __init__(self, name: string, size: int):
        self.name = name
        self.size = size


class Image(object):

    # TODO: consider to decouple images from Image descriptors
    def __init__(self, name: string, size: int):
        self.name = name
        self.size = size
        self.stored_in_device = None
        self.in_use_on_this_device = False
        self._storage_space_requirements = StorageSpaceRequirement(size)

    def storage_space_requirements(self) -> Requirement:
        return self._storage_space_requirements


class Microservice(object):

    def __init__(self, name: string, requirements: list[Requirement], image: Image, has_volumes=False,
                 volumes: list[Volume] = None, batch=False, length: int = -1):
        # Mandatory arguments (name, requirement, image)
        self._requirements = requirements
        self._name = name
        self._image = image

        # References to volumes (if any)
        if volumes is None:
            volumes = {}
        assert has_volumes == (len(volumes) > 0), "Error in the setting of Microservice volumes"
        self.has_volumes = has_volumes
        self._volumes = volumes

        # Information about length (if batch)
        assert batch == (length > 0), "Error in the setting of Microservice length"
        self.batch = batch
        self._length = length

        self._id = hash(self)

    @property
    def id(self) -> string:
        return self._id

    @property
    def name(self) -> string:
        return self._name

    @property
    def requirements(self) -> list[Requirement]:
        return self._requirements

    @property
    def image(self) -> Image:
        return self._image

    @property
    def volumes(self) -> list[Volume]:
        return self._volumes

    def length(self) -> int:
        return self._length

    def has_volumes(self) -> bool:
        return self.has_volumes

    def is_batch(self) -> bool:
        return self.batch


class Application(object):
    def __init__(self, name: string, components: list[Microservice]):
        self.components = components
        self.name = name

    def get_components(self) -> list[Microservice]:
        return self.components

    def get_name(self) -> string:
        return self.name
