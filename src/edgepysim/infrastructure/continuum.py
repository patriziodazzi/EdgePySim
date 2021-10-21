from edgepysim.orchestrator.orchestrator import GlobalOrchestrator
from edgepysim.infrastructure.cluster import ComputingInfrastructure


class ComputingContinuum(object):

    def __init__(self, datacenters: set[ComputingInfrastructure], orchestrator: GlobalOrchestrator):
        self.datacenters = datacenters
        self.orchestrator = orchestrator

    def get_datacenters(self) -> set[ComputingInfrastructure]:
        return self.datacenters
