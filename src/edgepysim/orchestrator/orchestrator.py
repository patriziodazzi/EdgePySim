from edgepysim import Orchestrator, Application, Microservice, Device, CloudDevice, EdgeDevice


class GlobalOrchestrator(Orchestrator):
    def __init__(self):
        super().__init__()

    def deploy(self, application: Application) -> bool:
        pass


class DomainOrchestrator(Orchestrator):
    def __init__(self, devices: list[Device]):
        super().__init__()
        self.resources = devices

    def deploy(self, services: list[Microservice]) -> bool:
        pass

    def list_of_suitable_devices(self, ms: Microservice) -> list[Device]:
        pass


class CloudOrchestrator(DomainOrchestrator):
    def __init__(self, cloud_resources: list[CloudDevice]):
        super().__init__(cloud_resources)

    def deploy(self, services: list[Microservice]) -> bool:
        pass


class EdgeOrchestrator(DomainOrchestrator):
    def __init__(self, edge_resources: list[EdgeDevice]):
        super().__init__(edge_resources)

    def deploy(self, services: list[Microservice]) -> bool:
        pass
