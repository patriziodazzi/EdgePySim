from edgepysim import *
import itertools
import networkx as nx

from edgepysim.device.base import NetworkSwitchRouter
from edgepysim.network.base import Network


class CloudAreaNetwork(Network):
    num_of_cans: int = 0

    def __init__(self, devices: list[CloudDevice], internal_bandwidth, external_bandwidth, is_routed=True,
                 gateway: Device = None):

        # Creates the network graph through superclass call
        super().__init__()
        self.is_routed = is_routed

        # If the cloud is rooted, check if it has a router, otherwise one is created. If the cloud is not rooted,
        # the first device in the cloud is "elected" gateway, i.e. the node delegated to external communication
        if self.is_routed:
            if gateway:
                self.gateway = gateway
            else:
                self.gateway = NetworkSwitchRouter(external_bandwidth)
                print(self.gateway)
        else:
            self.gateway = devices[0]

        # Generates a name for the network
        CloudAreaNetwork.num_of_cans += 1
        self.name = str("CAN." + str(CloudAreaNetwork.num_of_cans))

        # Adds the devices to the network and links devices to the router (not performed is the router is one of the
        # cloud devices)
        for device in devices:
            self.graph.add_node(device)
            if self.gateway not in devices:
                self.graph.add_edge(device, self.gateway)

        # Links all the devices one each others
        self.internal_bandwidth = internal_bandwidth
        for a in itertools.combinations(devices, 2):
            self.graph.add_edge(a[0], a[1], weight=self.internal_bandwidth)

    def add_device(self, device: Device) -> bool:

        if device in self.graph.nodes:
            return False

        self.graph.add_node(device)

        for neighbor in self.graph.nodes:
            self.graph.add_edge(device, neighbor, weight=self.internal_bandwidth)
        return True

    def remove_device(self, node: Device) -> bool:
        self.graph.remove_node(node)
        return True

    def get_gateway(self):
        return self.gateway
