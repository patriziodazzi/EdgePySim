import abc
import string
from typing import Any

from simulator1edge.network.base import Network
from simulator1edge.network.core import ComputingContinuumNetwork
from simulator1edge.orchestrator.concrete import ContinuumOrchestrator
from simulator1edge.infrastructure.cluster import ComputingInfrastructure


class ComputingContinuum(object):

    def __init__(self, datacenters: list[ComputingInfrastructure], orchestrator: ContinuumOrchestrator,
                 network: Network):
        self._datacenters = datacenters
        self._orchestrator = orchestrator
        self._network = network

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
    def orchestrator(self) -> ContinuumOrchestrator:
        return self._orchestrator

    @orchestrator.setter
    def orchestrator(self, value: ContinuumOrchestrator):
        self._orchestrator = value



