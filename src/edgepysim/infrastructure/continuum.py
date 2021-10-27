import networkx as nx
import networkx.algorithms.operators.binary as nx_algo
from edgepysim.network.base import Network
from edgepysim.orchestrator.concrete import GlobalOrchestrator
from edgepysim.infrastructure.cluster import ComputingInfrastructure


class ComputingContinuum(object):

    def __init__(self, datacenters: list[ComputingInfrastructure], orchestrator: GlobalOrchestrator, network: Network):
        self._datacenters = datacenters
        self._orchestrator = orchestrator
        self._network = network
        self.__compose_networks__()

    @property
    def datacenters(self) -> list[ComputingInfrastructure]:
        return self._datacenters

    @datacenters.setter
    def datacenters(self, value: list[ComputingInfrastructure]):
        self._datacenters = value

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, value):
        self._network = value

    @property
    def orchestrator(self) -> GlobalOrchestrator:
        return self._orchestrator

    @orchestrator.setter
    def orchestrator(self, value: GlobalOrchestrator):
        self._orchestrator = value

    def __compose_networks__(self):
        # TODO: move network composition business code inside continuum network class
        graph = self.network.graph
        for computing_infrastructure in self.datacenters:
            graph = nx_algo.compose(graph, computing_infrastructure.network.graph)

        self.network.graph = graph
