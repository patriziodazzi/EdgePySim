import networkx as nx


class Network(object):

    def __init__(self):
        self._graph = nx.Graph()

    @property
    def graph(self) -> nx.Graph:
        return self._graph

    @graph.setter
    def graph(self, value: nx.Graph):
        self._graph = value
