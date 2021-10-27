import string

from abc import ABC, abstractmethod
from typing import Any

from edgepysim.device.base import Device
from edgepysim.infrastructure.cluster import ComputingInfrastructure, Cloud
from edgepysim.network.areanetwork import CloudAreaNetwork
from edgepysim.orchestrator.base import Orchestrator
from edgepysim.orchestrator.concrete import CloudOrchestrator


class ComputingInfrastructureFactory(ABC):
    """Factory class for creating instances of ComputingInfrastructure and the associated orchestrator and network

    Methods
    -------
    __create_instance__()
        Creates instances of ComputingInfrastructure and the associated orchestrator and network.
    get_computing_infrastructure()
        Returns the ComputingInfrastructure created.
    get_orchestrator()
        Returns the Orchestrator associated to the ComputingInfrastructure.
    """

    def __init__(self, features: dict[string, Any] = None) -> None:
        """
        Parameters
        ----------
        features : dict[string, Any], optional
            The name of the animal
        """

        self.features = features

        if 'devices' in features:
            self._devices = features['devices']
        else:
            self._devices = None

        # If network is provided, does not create it
        if 'network' in self.features:
            self._network = self.features['network']
        else:
            self._network = None

        # If orchestrator is provided, does not create it
        if 'orchestrator' in self.features:
            self._orchestrator = self.features['orchestrator']
        else:
            self._orchestrator = None

    @property
    def devices(self) -> list[Device]:
        return self._devices

    @devices.setter
    def devices(self, value: list[Device]):
        self._orchestrator = value

    @property
    def orchestrator(self) -> Orchestrator:
        return self._orchestrator

    @orchestrator.setter
    def orchestrator(self, value: Orchestrator):
        self._orchestrator = value

    @property
    def network(self) -> CloudAreaNetwork:
        return self._network

    @network.setter
    def network(self, value: CloudAreaNetwork):
        self._network = value

    @abstractmethod
    def do_create_computing_instance(self) -> ComputingInfrastructure:
        raise NotImplementedError("You should implement this!")


class CloudFactory(ComputingInfrastructureFactory):

    def __init__(self, features: dict[string, Any] = None):
        super().__init__(features)

        # If internal_bandwidth is provided, uses it, otherwise uses the standard value
        if 'internal_bandwidth' in self.features:
            self._internal_bandwidth = self.features['internal_bandwidth']

        # If external_bandwidth is provided, uses it, otherwise uses the standard value
        if 'external_bandwidth' in self.features:
            self._external_bandwidth = self.features['external_bandwidth']

        # If is_routed is provided, uses it, otherwise uses the standard value
        if 'is_routed' in self.features:
            self._is_routed = self.features['is_routed']

        # If gateway is provided, uses it, otherwise uses the standard value
        if 'gateway' in self.features:
            self._gateway = self.features['gateway']

    @property
    def internal_bandwidth(self) -> int:
        return self._internal_bandwidth

    @internal_bandwidth.setter
    def internal_bandwidth(self, value: int):
        self._internal_bandwidth = value

    @property
    def external_bandwidth(self) -> int:
        return self._external_bandwidth

    @external_bandwidth.setter
    def external_bandwidth(self, value: int):
        self._external_bandwidth = value

    @property
    def is_routed(self) -> bool:
        return self._is_routed

    @is_routed.setter
    def is_routed(self, value: bool):
        self._is_routed = value

    @property
    def gateway(self) -> Device:
        return self._gateway

    @gateway.setter
    def gateway(self, value: Device):
        self._gateway = value

    def do_create_computing_instance(self) -> ComputingInfrastructure:

        self.gateway = None
        self.internal_bandwidth = 1000
        self.external_bandwidth = 100
        self.is_routed = True


        # if network has not been provided, creates it
        if not self.network:

            # If gateway is provided, specifies it, otherwise uses the shorter constructor
            if self.gateway:
                self.network = CloudAreaNetwork(self.resources, self.internal_bandwidth, self.external_bandwidth,
                                                self.is_routed, self.gateway)
            else:
                self.network = CloudAreaNetwork(self.resources, self.internal_bandwidth, self.external_bandwidth,
                                                self.is_routed)

        # if orchestrator has not been provided, creates it
        if not self.orchestrator:
            # If orchestrator is provided, specifies it, otherwise uses the shorter constructor
            self.orchestrator = CloudOrchestrator(self.resources, self.network)

        self.computing_infrastructure = Cloud(self.resources, self.orchestrator, self.network)

        return self.computing_infrastructure
