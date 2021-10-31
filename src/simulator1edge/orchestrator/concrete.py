from typing import Union, cast

from simulator1edge.application.base import Application, Microservice
from simulator1edge.infrastructure.cluster import ComputingInfrastructure
from simulator1edge.device.base import Device
from simulator1edge.network.base import Network
from simulator1edge.orchestrator.base import Orchestrator


class ContinuumOrchestrator(Orchestrator):
    def __init__(self, computing_infrastructures: list[ComputingInfrastructure], network: Network):
        super().__init__(computing_infrastructures, network)
        self._computing_infrastructures = computing_infrastructures

    def deploy(self, application: Application) -> bool:
        pass


class DomainOrchestrator(Orchestrator):
    def __init__(self, devices: list[Device], network: Network):
        super().__init__(devices, network)

    def deploy(self, services: list[Microservice]) -> bool:
        result: bool = True
        for service in services:
            candidate_resources = self.list_of_candidates(service)
            image_locations = self._find_image(service.image.name)
            result = result and self._place_service(service, candidate_resources, image_locations)
        return result

    def list_of_candidates(self, ms: Microservice) -> list[Device]:
        suitable_devices = \
            [d for d in self.resources if (Orchestrator.is_device_satisfying_all_requirements(d, ms.requirements))]
        return suitable_devices

    # TODO add the second part: image located outside the cloud
    def _find_image(self, image_name) -> (list[Device], list[Union[Device, ComputingInfrastructure]]):
        image_locations: list = [i for i in self.resources if (image_name in cast(Device, i).images)]
        return image_locations, None

    def _place_service(self, service: Microservice, candidate_resources: list[Device],
                       image_locations: (list[Device], list[Union[Device, ComputingInfrastructure]])) -> bool:

        # intersect resource candidates with resources having images
        local_image_locations: list = image_locations[0]
        print(local_image_locations)
        available_candidates_with_image = list(filter(lambda x: x in candidate_resources, local_image_locations))
        if not available_candidates_with_image:
            target_device = candidate_resources.pop()
            if local_image_locations:
                if target_device.has_enough_space_for_image(service.image.storage_space_requirements().rd.value):
                    target_device.retrieve_image_from(service.image, local_image_locations[0])
        else:
            target_device = available_candidates_with_image.pop()

        target_device.start_microservice(service)
        return True


class CloudOrchestrator(DomainOrchestrator):
    def __init__(self, cloud_resources: list[Device], network: Network):
        super().__init__(cloud_resources, network)

    def deploy(self, services: list[Microservice]) -> bool:
        super().deploy(services)


class EdgeOrchestrator(DomainOrchestrator):
    def __init__(self, edge_resources: list[Device], network: Network):
        super().__init__(edge_resources, network)

    def deploy(self, services: list[Microservice]) -> bool:
        pass
