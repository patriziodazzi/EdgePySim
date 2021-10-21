from edgepysim import *

if __name__ == '__main__':

    # Create Application
    img = Image("ubuntu", 5000)
    reqs = [StorageSpaceRequirement("2000"),
            NetworkBandwidthRequirement("200"),
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

