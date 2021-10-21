from edgepysim import *

if __name__ == '__main__':

    # Create Application
    img = Image("ubuntu", 5000)
    reqs = [StorageSpaceRequirement("1500"),
            NetworkBandwidthRequirement("10"),
            MemoryAmountRequirement("512")]
    ms = Microservice("ms1", reqs, img)
    app = Application("Linux", [ms])

    # Create resources
    dev_res = [StorageSpaceResourceDescriptor("2000"),
               NetworkBandwidthResourceDescriptor("100"),
               MemoryAmountResourceDescriptor("768")]

    devices = []
    for x in range(10):
        dv = CloudDevice("rack01", dev_res)
        devices.append(dv)

    # Create cloud
    cloud_orchestrator = CloudOrchestrator(devices)
    c = Cloud(devices, cloud_orchestrator)

    iss = Orchestrator.is_device_satisfying_all_requirements(devices[0], ms.requirements)

    print(iss)
    ret = cloud_orchestrator.list_of_suitable_devices(ms)
    for x in ret:
        print(x.get_name())



