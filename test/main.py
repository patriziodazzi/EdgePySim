import networkx as nx
import matplotlib.pyplot as plt

from simulator1edge.application.base import Image, Microservice, Application
from simulator1edge.device.base import NetworkSwitchRouter, CloudDevice
from simulator1edge.device.generator import CloudDeviceFactory
from simulator1edge.infrastructure.cluster import Cloud
from simulator1edge.infrastructure.continuum import ComputingContinuum
from simulator1edge.infrastructure.generator import CloudFactory, FeatureType
from simulator1edge.network.areanetwork import CloudAreaNetwork
from simulator1edge.network.base import Network
from simulator1edge.network.general import EndToEndNetwork, BackboneNetwork
from simulator1edge.orchestrator.concrete import CloudOrchestrator, GlobalOrchestrator
from simulator1edge.resource.descriptor import StorageSpaceResourceDescriptor, NetworkBandwidthResourceDescriptor, \
    MemoryAmountResourceDescriptor
from simulator1edge.resource.requirement import StorageSpaceRequirement, NetworkBandwidthRequirement, MemoryAmountRequirement


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

    for d in devices: print(d)

    cloud1 = CloudFactory({FeatureType.DEVICES: devices,
                           FeatureType.GATEWAY: NetworkSwitchRouter(1000),
                           FeatureType.INTERNAL_NETWORK_BANDWIDTH: 1000}).do_create_computing_instance()

    # Create cloud#2
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud2"})
    cloud2 = CloudFactory({FeatureType.DEVICES: devices,
                           FeatureType.GATEWAY: NetworkSwitchRouter(1000),
                           FeatureType.INTERNAL_NETWORK_BANDWIDTH: 1000}).do_create_computing_instance()
    # Create cloud#3
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud3"})
    cloud3 = CloudFactory({FeatureType.DEVICES: devices,
                           FeatureType.INTERNAL_NETWORK_BANDWIDTH: 100,
                           FeatureType.EXTERNAL_NETWORK_BANDWIDTH: 1000,
                           FeatureType.GATEWAY: NetworkSwitchRouter(10),
                           FeatureType.ORCHESTRATOR: CloudOrchestrator}).do_create_computing_instance()

    # Create Continuum
    net = BackboneNetwork()
    continuum = ComputingContinuum([cloud1,
                                    cloud2,
                                    cloud3],
                                   GlobalOrchestrator(net), net)

    EndToEndNetwork(cloud1.network.gateway,
                    cloud2.network.gateway,
                    continuum.network.graph, 10)

    EndToEndNetwork(cloud2.network.gateway,
                    cloud3.network.gateway,
                    continuum.network.graph, 10)

    EndToEndNetwork(cloud1.network.gateway,
                    cloud3.network.gateway,
                    continuum.network.graph, 10)


    # Show network graph
    f = plt.figure()
    nx.draw(continuum.network.graph,
            pos=nx.nx_pydot.graphviz_layout(continuum.network.graph, prog="neato"),
            node_size=120, node_color='red', linewidths=0.01, font_size=6, font_weight='bold',
            with_labels=True, ax=f.add_subplot(111))
    f.savefig("ciccio.png")
