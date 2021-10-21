from edgepysim import *

if __name__ == '__main__':

    reqs = [StorageSpaceRequirement("2000"),
            NetworkBandwidthRequirement("200"),
            MemoryAmountRequirement("512")]

    dev_res = [StorageSpaceResourceDescriptor("2000"),
               NetworkBandwidthResourceDescriptor("100"),
               MemoryAmountResourceDescriptor("768")]

    devices = []
    for x in range(10):
        dv = CloudDevice("rack01", dev_res)
        devices.append(dv)

    c = Cloud(devices, None)

    requirements = RequirementSet(reqs)

    img = Image("ubuntu", 5000)
    ms = Microservice("ms1", reqs, img)
    app = Application("Linux", {ms})

    # print(requirements.are_satisfied_by_device(dv))

    # print(dv.get_name())
