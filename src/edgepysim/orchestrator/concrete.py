from edgepysim import Orchestrator, Application, Microservice, Device, CloudDevice, EdgeDevice
from edgepysim.network.base import Network


class GlobalOrchestrator(Orchestrator):
    def __init__(self, network: Network):
        super().__init__(network)

    def deploy(self, application: Application) -> bool:
        pass


class DomainOrchestrator(Orchestrator):
    def __init__(self, devices: list[Device], network: Network):
        super().__init__(network)
        self.resources = devices

    def deploy(self, services: list[Microservice]) -> bool:
        pass

    def list_of_suitable_devices(self, ms: Microservice) -> list[Device]:
        suitable_devices = [d for d in self.resources
                            if (Orchestrator.is_device_satisfying_all_requirements(d, ms.requirements))]
        return suitable_devices


class CloudOrchestrator(DomainOrchestrator):
    def __init__(self, cloud_resources: list[CloudDevice], network: Network):
        super().__init__(cloud_resources, network)

    def deploy(self, services: list[Microservice]) -> bool:
        pass


class EdgeOrchestrator(DomainOrchestrator):
    def __init__(self, edge_resources: list[EdgeDevice], network: Network):
        super().__init__(edge_resources, network)

    def deploy(self, services: list[Microservice]) -> bool:
        pass
