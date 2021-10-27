import networkx as nx
import matplotlib.pyplot as plt

from edgepysim.application.base import Image, Microservice, Application
from edgepysim.device.base import NetworkSwitchRouter, CloudDevice
from edgepysim.device.generator import CloudDeviceFactory
from edgepysim.infrastructure.cluster import Cloud
from edgepysim.infrastructure.continuum import ComputingContinuum
from edgepysim.infrastructure.generator import CloudFactory
from edgepysim.network.areanetwork import CloudAreaNetwork
from edgepysim.network.base import Network
from edgepysim.network.general import EndToEndNetwork, BackboneNetwork
from edgepysim.orchestrator.concrete import CloudOrchestrator, GlobalOrchestrator
from edgepysim.resource.descriptor import StorageSpaceResourceDescriptor, NetworkBandwidthResourceDescriptor, \
    MemoryAmountResourceDescriptor
from edgepysim.resource.requirement import StorageSpaceRequirement, NetworkBandwidthRequirement, MemoryAmountRequirement


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
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud1"})
    cloud1 = CloudFactory({'devices': devices,
                           'infrastructure_entry_point': NetworkSwitchRouter(1000),
                           'internal_network_bandwidth': 1000})

    # Create cloud#2
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud2"})
    cloud2 = CloudFactory({'devices': devices,
                           'infrastructure_entry_point': NetworkSwitchRouter(1000),
                           'internal_network_bandwidth': 1000})
    # Create cloud#3
    devices = CloudDeviceFactory().create_devices([(hpc_res, 2), (avg_res, 2), (low_res, 1)], {'cloud_name': "cloud3"})
    cloud3 = CloudFactory({'devices': devices,
                           'internal_network_bandwidth': 100,
                           'external_network_bandwidth': 1000,
                           'gateway': NetworkSwitchRouter(10),
                           'orchestrator': CloudOrchestrator})

    # Create Continuum
    net = BackboneNetwork()
    continuum = ComputingContinuum([cloud1.get_computing_infrastructure(),
                                    cloud2.get_computing_infrastructure(),
                                    cloud3.get_computing_infrastructure()],
                                   GlobalOrchestrator(net), net)

    EndToEndNetwork(cloud1.get_network().get_gateway(),
                    cloud2.get_network().get_gateway(),
                    continuum.network.graph, 10)

    EndToEndNetwork(cloud2.get_network().get_gateway(),
                    cloud3.get_network().get_gateway(),
                    continuum.network.graph, 10)

    EndToEndNetwork(cloud1.get_network().get_gateway(),
                    cloud3.get_network().get_gateway(),
                    continuum.network.graph, 10)

    # Show network graph
    f = plt.figure()
    nx.draw(continuum.network.graph,
            pos=nx.nx_pydot.graphviz_layout(continuum.network.graph, prog="neato"),
            node_size=120, node_color='red', linewidths=0.01, font_size=6, font_weight='bold',
            with_labels=True, ax=f.add_subplot(111))
    f.savefig("ciccio.png")

