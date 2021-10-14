from edgepysim.infrastructure import EdgeCluster, Cloud


class Orchestrator(object):
    def __init__(self):
        pass


class GlobalOrchestrator(Orchestrator):
    def __init__(self):
        super().__init__()


class CloudOrchestrator(Orchestrator):
    def __init__(self, cloud: Cloud):
        super().__init__()


class EdgeOrchestrator(Orchestrator):
    def __init__(self, edge_cluster: EdgeCluster):
        super().__init__()
