from simulator1edge import *
import networkx as nx

from simulator1edge.network.base import Network


class EndToEndNetwork(Network):

    # TODO change parameters to encapsulate the graph
    def __init__(self, end_point_a: Device, end_point_b: Device, network_graph: nx.Graph, bandwidth: int):
        super().__init__()
        network_graph.add_node(end_point_a)
        network_graph.add_node(end_point_b)
        network_graph.add_edge(end_point_a, end_point_b, bandwidth=bandwidth)


class BackboneNetwork(Network):

    def __init__(self):
        super().__init__()
