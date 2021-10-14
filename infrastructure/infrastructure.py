from device.device import CloudDevice, EdgeDevice
from resource.resource import Resource


class ComputingInfrastructure(object):
    def __init__(self, resources: set[Resource], orchestrator: Orchestrator):
        self.resources = resources
        self.orchestrator = orchestrator

    def get_resources(self) -> set[Resource]:
        pass


class Cloud(ComputingInfrastructure):
    def __init__(self, resources: set[Resource], orchestrator: Orchestrator):
        super().__init__(resources, orchestrator)

    def get_resources(self) -> set[CloudDevice]:
        pass


class EdgeCluster(ComputingInfrastructure):
    def __init__(self, resources: set[Resource], orchestrator: Orchestrator):
        super().__init__(resources, orchestrator)

    def get_resources(self) -> set[EdgeDevice]:
        pass
