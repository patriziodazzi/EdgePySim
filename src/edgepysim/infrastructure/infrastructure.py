# from edgepysim.orchestrator.orchestrator import Orchestrator
# from edgepysim.device.device import CloudDevice, EdgeDevice
# from edgepysim.resource.resource import Resource

from edgepysim import *


class ComputingInfrastructure(object):
    def __init__(self, resources: set[ResourceDescriptor], orchestrator: Orchestrator):
        self.resources = resources
        self.orchestrator = orchestrator

    def get_resources(self) -> set[ResourceDescriptor]:
        pass


class Cloud(ComputingInfrastructure):
    def __init__(self, resources: set[ResourceDescriptor], orchestrator: Orchestrator):
        super().__init__(resources, orchestrator)

    def get_resources(self) -> set[CloudDevice]:
        pass


class EdgeCluster(ComputingInfrastructure):
    def __init__(self, resources: set[ResourceDescriptor], orchestrator: Orchestrator):
        super().__init__(resources, orchestrator)

    def get_resources(self) -> set[EdgeDevice]:
        pass
