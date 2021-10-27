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


class IComputingContinuumBuilder(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def create_network(self, features: dict[string, Any]):
        pass

    @abc.abstractmethod
    def create_orchestrator(self, features: dict[string, Any]):
        pass

    @abc.abstractmethod
    def create_continuum(self, features: dict[string, Any]):
        pass

    @abc.abstractmethod
    def result(self):
        pass


class ComputingContinuumBuildDirector(object):
    CMP_CNT_RES_FEAT = 'computing_continuum_resources'

    def __init__(self, builder: IComputingContinuumBuilder):
        self._builder = builder

    def construct(self, features: dict[string, Any]):
        self._builder.create_network(features)
        self._builder.create_orchestrator(features)
        self._builder.create_continuum(features)

    @property
    def result(self):
        return self._builder.result


class ComputingContinuumBuilder(IComputingContinuumBuilder):

    def __init__(self):
        self._orchestrator = None
        self._network = None
        self._resources = None
        self._computing_infrastructure = None

    def create_network(self, features: dict[string, Any]):
        self._resources: list[ComputingInfrastructure] = features[ComputingContinuumBuildDirector.CMP_CNT_RES_FEAT]
        self._network = ComputingContinuumNetwork(self._resources)
        self._network.do_link_computing_infrastructures({ComputingContinuumNetwork.TPLGY_FEAT: ComputingContinuumNetwork.CLIQ})

    def create_orchestrator(self, features: dict[string, Any]):
        self._orchestrator = ContinuumOrchestrator(self._resources, self._network)

    def create_continuum(self, features: dict[string, Any]):
        self._computing_infrastructure = ComputingContinuum(self._resources, self._orchestrator, self._network)

    @property
    def result(self):
        return self._computing_infrastructure
