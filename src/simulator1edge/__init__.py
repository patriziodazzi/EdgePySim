# Forward declarations

from simulator1edge.resource.descriptor import ResourceType, ResourceDescriptor, IntegerResourceDescriptor, \
    MemoryAmountResourceDescriptor, NetworkBandwidthResourceDescriptor, ProcessingCapacityResourceDescriptor, \
    StorageSpaceResourceDescriptor

from simulator1edge.resource.requirement import Requirement, RequirementSet, IntegerRequirement, \
    MemoryAmountRequirement, NetworkBandwidthRequirement, ProcessingCapacityResourceRequirement, StorageSpaceRequirement

from simulator1edge.application.base import Application, Image, Microservice, Volume

from simulator1edge.device.base import Device, CloudDevice, EdgeDevice

from simulator1edge.orchestrator.base import Orchestrator
from simulator1edge.orchestrator.concrete import GlobalOrchestrator, EdgeOrchestrator, CloudOrchestrator

from simulator1edge.infrastructure.cluster import Cloud, ComputingInfrastructure, EdgeCluster
from simulator1edge.infrastructure.continuum import ComputingContinuum
