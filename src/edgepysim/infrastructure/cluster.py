import abc

from edgepysim.device.base import Device, CloudDevice, EdgeDevice
from edgepysim.network.areanetwork import CloudAreaNetwork
from edgepysim.network.base import Network
from edgepysim.orchestrator.base import Orchestrator
from edgepysim.orchestrator.concrete import CloudOrchestrator, EdgeOrchestrator


class ComputingInfrastructure(abc.ABC):
    def __init__(self, devices: list[Device], orchestrator: Orchestrator, network: Network):
        self._devices = devices
        self._orchestrator = orchestrator
        self._network = network

    @property
    def devices(self) -> list[Device]:
        return self._devices

    @devices.setter
    def devices(self, value: list[Device]):
        self._devices = value

    @property
    def orchestrator(self) -> Orchestrator:
        return self._orchestrator

    @orchestrator.setter
    def orchestrator(self, value: Orchestrator):
        self._orchestrator = value

    @property
    def network(self) -> Network:
        return self._network

    @network.setter
    def network(self, value: Network):
        self._network = value


class Cloud(ComputingInfrastructure):
    def __init__(self, devices: list[CloudDevice], orchestrator: CloudOrchestrator, network: CloudAreaNetwork):
        super().__init__(devices, orchestrator, network)


class EdgeCluster(ComputingInfrastructure):
    def __init__(self, devices: list[EdgeDevice], orchestrator: EdgeOrchestrator, network: Network):
        super().__init__(devices, orchestrator, network)
