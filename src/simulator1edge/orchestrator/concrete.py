from simulator1edge.application.base import Application, Microservice
from simulator1edge.infrastructure.cluster import ComputingInfrastructure
from simulator1edge.device.base import Device
from simulator1edge.network.base import Network
from simulator1edge.orchestrator.base import Orchestrator


class ContinuumOrchestrator(Orchestrator):
    def __init__(self, computing_infrastructures: list[ComputingInfrastructure], network: Network):
        super().__init__(computing_infrastructures, network)
        self._computing_infrastructures = computing_infrastructures

    def deploy(self, application: Application) -> bool:
        pass


class DomainOrchestrator(Orchestrator):
    def __init__(self, devices: list[Device], network: Network):
        super().__init__(devices, network)

    def deploy(self, services: list[Microservice]) -> bool:
        pass

    def list_of_candidates(self, ms: Microservice) -> list[Device]:
        suitable_devices = [d for d in self.resources
                            if (Orchestrator.is_device_satisfying_all_requirements(d, ms.requirements))]
        return suitable_devices


class CloudOrchestrator(DomainOrchestrator):
    def __init__(self, cloud_resources: list[Device], network: Network):
        super().__init__(cloud_resources, network)

    def deploy(self, services: list[Microservice]) -> bool:
        pass


class EdgeOrchestrator(DomainOrchestrator):
    def __init__(self, edge_resources: list[Device], network: Network):
        super().__init__(edge_resources, network)

    def deploy(self, services: list[Microservice]) -> bool:
        pass
