# Forward declarations

from edgepysim.base.definition import ResourceType, Orchestrator
from edgepysim.resource.descriptor import ResourceDescriptor, IntegerResourceDescriptor, \
    MemoryAmountResourceDescriptor, NetworkBandwidthResourceDescriptor, ProcessingCapacityResourceDescriptor, \
    StorageSpaceResourceDescriptor
from edgepysim.resource.requirement import Requirement, RequirementSet, IntegerRequirement, \
    MemoryAmountRequirement, NetworkBandwidthRequirement, ProcessingCapacityResourceRequirement, StorageSpaceRequirement
from edgepysim.application.application import Application, Image, Microservice, Volume
from edgepysim.device.device import Device, CloudDevice, EdgeDevice
from edgepysim.infrastructure.cluster import Cloud, ComputingInfrastructure, EdgeCluster
from edgepysim.orchestrator.orchestrator import GlobalOrchestrator, EdgeOrchestrator, CloudOrchestrator
from edgepysim.infrastructure.continuum import ComputingContinuum
