from edgepysim import *


if __name__ == '__main__':

    reqs = {StorageSpaceRequirement("2000"), NetworkBandwidthRequirement("200"), MemoryAmountRequirement("512")}

    dev_res = {ResourceType.STORAGE: IntegerResourceDescriptor(ResourceType.STORAGE, "2500"),
               ResourceType.NETWORK_BANDWIDTH: IntegerResourceDescriptor(ResourceType.NETWORK_BANDWIDTH, "1000"),
               ResourceType.MEMORY_AMOUNT: IntegerResourceDescriptor(ResourceType.MEMORY_AMOUNT, "1024"),
               ResourceType.COMPUTING_CAPACITY: IntegerResourceDescriptor(ResourceType.MEMORY_AMOUNT, "800")}

    dv = CloudDevice("rack01", dev_res)
    requirements = RequirementSet(reqs)

    print(requirements.are_satisfied_by_device(dv))
