
from simulator1edge.device.base import Device
from simulator1edge.network.base import Network
from simulator1edge.resource.requirement import Requirement


class Orchestrator(object):
    def __init__(self, resources: list, network: Network):
        self._network = network
        self._resources = resources

    @property
    def resources(self):
        return self._resources

    @property
    def network(self):
        return self._network

    @staticmethod
    def is_device_satisfying_requirement(dev: Device, req: Requirement) -> bool:
        available_resources = dev.get_resources()

        actual_resource = None
        for i_rt, i_rd in available_resources.items():
            if i_rt == req.rd.res_type:
                actual_resource = i_rd

        if not actual_resource:
            return False

        return req.is_satisfied_by_resource(actual_resource)

    @staticmethod
    def is_device_satisfying_all_requirements(dev: Device, rs: list[Requirement]) -> bool:
        return all(map(lambda r: Orchestrator.is_device_satisfying_requirement(dev, r), rs))
