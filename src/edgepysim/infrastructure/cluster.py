from edgepysim import *


class ComputingInfrastructure(object):
    def __init__(self, devices: list[Device], orchestrator: Orchestrator):
        self.devices = devices
        self.orchestrator = orchestrator

    def get_devices(self) -> list[ResourceDescriptor]:
        pass


class Cloud(ComputingInfrastructure):
    def __init__(self, devices: list[CloudDevice], orchestrator: Orchestrator):
        super().__init__(devices, orchestrator)

    def get_devices(self) -> list[CloudDevice]:
        pass


class EdgeCluster(ComputingInfrastructure):
    def __init__(self, devices: list[EdgeDevice], orchestrator: Orchestrator):
        super().__init__(devices, orchestrator)

    def get_devices(self) -> list[EdgeDevice]:
        pass
