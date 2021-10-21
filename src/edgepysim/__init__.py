# Forward declarations
class ResourceType:
    pass


class ResourceDescriptor:
    pass


class Image:
    pass


class Microservice:
    pass


class Orchestrator:
    pass


from edgepysim.device.device import Device, CloudDevice, EdgeDevice
from edgepysim.resource.resource import ResourceType, ResourceDescriptor, IntegerResourceDescriptor
from edgepysim.resource.requirement import Requirement, GenericIntegerRequirement, MemoryAmountRequirement, \
    NetworkBandwidthRequirement, ProcessingCapacityResourceRequirement, StorageSpaceRequirement
from edgepysim.application.application import Application, Image, Microservice, Volume
from edgepysim.infrastructure.infrastructure import Cloud, ComputingInfrastructure, EdgeCluster
from edgepysim.infrastructure.continuum import ComputingContinuum
from edgepysim.orchestrator.orchestrator import Orchestrator, GlobalOrchestrator, EdgeOrchestrator, CloudOrchestrator
