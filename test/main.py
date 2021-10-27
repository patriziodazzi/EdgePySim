import matplotlib.pyplot as plt
import networkx as nx

from simulator1edge.application.base import Image, Microservice, Application
from simulator1edge.device.concrete import NetworkSwitchRouter
from simulator1edge.device.generator import CloudDeviceFactory
from simulator1edge.infrastructure.continuum import ComputingContinuumBuildDirector, ComputingContinuumBuilder
from simulator1edge.infrastructure.generator import CloudFactory, ComputingInfrastructureFactory
from simulator1edge.orchestrator.concrete import CloudOrchestrator
from simulator1edge.resource.descriptor import StorageSpaceResourceDescriptor, NetworkBandwidthResourceDescriptor, \
    MemoryAmountResourceDescriptor
from simulator1edge.resource.requirement import StorageSpaceRequirement, NetworkBandwidthRequirement, \
    MemoryAmountRequirement

if __name__ == '__main__':
    # Create Application
    reqs = [StorageSpaceRequirement("1500"), NetworkBandwidthRequirement("10"), MemoryAmountRequirement("512")]
    img = Image("ubuntu", 5000)
    ms = Microservice("ms1", reqs, img)
    app = Application("Linux", [ms])

    # Create resources
    hpc_res = [StorageSpaceResourceDescriptor("2000"),
               NetworkBandwidthResourceDescriptor("1000"),
               MemoryAmountResourceDescriptor("1024")]

    avg_res = [StorageSpaceResourceDescriptor("1000"),
               NetworkBandwidthResourceDescriptor("100"),
               MemoryAmountResourceDescriptor("512")]

    low_res = [StorageSpaceResourceDescriptor("500"),
               NetworkBandwidthResourceDescriptor("50"),
               MemoryAmountResourceDescriptor("256")]

    dev_res: list = [hpc_res, avg_res, low_res]

    # Create cloud#1
    devices = CloudDeviceFactory().create_devices([(hpc_res, 8), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud1"})
    cloud1 = CloudFactory({ComputingInfrastructureFactory.DEVS_FEAT: devices,
                           CloudFactory.GTWY_FEAT: NetworkSwitchRouter(1000),
                           CloudFactory.INTL_NET_BNDWDTH_FEAT: 1000}).do_create_computing_instance()

    # Create cloud#2
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud2"})
    cloud2 = CloudFactory({ComputingInfrastructureFactory.DEVS_FEAT: devices,
                           CloudFactory.GTWY_FEAT: NetworkSwitchRouter(1000),
                           CloudFactory.INTL_NET_BNDWDTH_FEAT: 1000}).do_create_computing_instance()
    # Create cloud#3
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud3"})
    cloud3 = CloudFactory({ComputingInfrastructureFactory.DEVS_FEAT: devices,
                           CloudFactory.INTL_NET_BNDWDTH_FEAT: 100,
                           CloudFactory.EXTL_NET_BNDWDTH_FEAT: 1000,
                           CloudFactory.GTWY_FEAT: NetworkSwitchRouter(10),
                           ComputingInfrastructureFactory.ORCHS_FEAT: CloudOrchestrator}).do_create_computing_instance()

    # Create Continuum
    features = {ComputingContinuumBuildDirector.CMP_CNT_RES_FEAT: [cloud1, cloud2, cloud3]}
    builder = ComputingContinuumBuildDirector(ComputingContinuumBuilder())
    builder.construct(features)
    cont = builder.result

    # Show network graph
    f = plt.figure()
    nx.draw(cont.network.graph,
            pos=nx.nx_pydot.graphviz_layout(cont.network.graph, prog="neato"),
            node_size=120, node_color='red', linewidths=0.01, font_size=6, font_weight='bold',
            with_labels=True, ax=f.add_subplot(111))
    f.savefig("ciccio.png")
