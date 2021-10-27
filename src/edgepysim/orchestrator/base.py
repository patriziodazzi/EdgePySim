from edgepysim import *
from edgepysim.network.base import Network


class Orchestrator(object):
    def __init__(self, network: Network):
        self.network = network

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
