import string
from resource.resource import Resource


class Device(object):

    def __init__(self, resources: set[Resource]):
        self.resources = resources

    def get_resources(self) -> set[Resource]:
        pass


class EdgeDevice(Device):

    def __init__(self, position: tuple[float, float], resources: set[Resource]):
        super().__init__(resources)
        self.position = position

    def get_position(self) -> tuple[float, float]:
        return self.position


class CloudDevice(Device):

    def __init__(self, rack: string, resources: set[Resource]):
        super().__init__(resources)
        self.rack = rack

    def get_rack(self) -> string:
        return self.rack
