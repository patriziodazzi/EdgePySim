import string

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, cast

from simulator1edge.device.base import Device, CloudDevice
from simulator1edge.infrastructure.cluster import ComputingInfrastructure, Cloud
from simulator1edge.network.areanetwork import CloudAreaNetwork
from simulator1edge.orchestrator.base import Orchestrator
from simulator1edge.orchestrator.concrete import CloudOrchestrator


class FeatureType(str, Enum):
    STORAGE = 'storage'
    NETWORK = 'network'
    DEVICES = 'devices'
    EXTERNAL_NETWORK_BANDWIDTH = 'external_bandwidth'
    INTERNAL_NETWORK_BANDWIDTH = 'internal_bandwidth'
    ORCHESTRATOR = 'orchestrator'
    GATEWAY = 'gateway'
    IS_ROUTED = 'is_routed'


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

        if FeatureType.DEVICES in features:
            self._devices = features[FeatureType.DEVICES]
        else:
            self._devices = None

        # If network is provided, does not create it
        if FeatureType.NETWORK in self.features:
            self._network = self.features[FeatureType.NETWORK]
        else:
            self._network = None

        # If orchestrator is provided, does not create it
        if FeatureType.ORCHESTRATOR in self.features:
            self._orchestrator = self.features[FeatureType.ORCHESTRATOR]
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

    # Standard Values
    __STD_INTL_BANDWIDTH = 100
    __STD_EXTL_BANDWIDTH = 100
    __STD_IS_RTD = True
    __STD_GTWY = None

    def __init__(self, features: dict[string, Any] = None):
        super().__init__(features)

        # If internal_bandwidth is provided, uses it, otherwise uses the standard value
        if FeatureType.INTERNAL_NETWORK_BANDWIDTH in self.features:
            self._internal_bandwidth = self.features[FeatureType.INTERNAL_NETWORK_BANDWIDTH]
        else:
            self._internal_bandwidth = CloudFactory.__STD_INTL_BANDWIDTH

        # If external_bandwidth is provided, uses it, otherwise uses the standard value
        if FeatureType.EXTERNAL_NETWORK_BANDWIDTH in self.features:
            self._external_bandwidth = self.features[FeatureType.EXTERNAL_NETWORK_BANDWIDTH]
        else:
            self._external_bandwidth = CloudFactory.__STD_EXTL_BANDWIDTH

        # If is_routed is provided, uses it, otherwise uses the standard value
        if FeatureType.IS_ROUTED in self.features:
            self._is_routed = self.features[FeatureType.IS_ROUTED]
        else:
            self._is_routed = CloudFactory.__STD_IS_RTD

        # If gateway is provided, uses it, otherwise uses the standard value
        if FeatureType.GATEWAY in self.features:
            self._gateway = self.features[FeatureType.GATEWAY]
        else:
            self._gateway = CloudFactory.__STD_GTWY

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

        # if network has not been provided, creates it
        if not self.network:

            # If gateway is provided, specifies it, otherwise uses the shorter constructor
            if self.gateway:
                self.network = CloudAreaNetwork(cast(list[CloudDevice], self.devices), self.internal_bandwidth,
                                                self.external_bandwidth, self.is_routed, self.gateway)
            else:
                self.network = CloudAreaNetwork(cast(list[CloudDevice], self.devices), self.internal_bandwidth,
                                                self.external_bandwidth, self.is_routed)

        # if orchestrator has not been provided, creates it
        if not self.orchestrator:
            # If orchestrator is provided, specifies it, otherwise uses the shorter constructor
            self.orchestrator = CloudOrchestrator(cast(list[CloudDevice], self.devices), self.network)

        self.computing_infrastructure = Cloud(cast(list[CloudDevice], self.devices),
                                              cast(CloudOrchestrator, self.orchestrator), self.network)

        return self.computing_infrastructure
