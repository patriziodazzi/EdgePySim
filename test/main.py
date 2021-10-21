# This is a sample Python script.
import simpy

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from edgepysim.application.application import Microservice
# from edgepysim.resource.resource import ResourceType, IntegerResourceDescriptor
# from edgepysim.resource.requirement import GenericIntegerRequirement

from edgepysim import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    env = simpy.Environment()

    env.process(clock(env, 'fast', 0.5))
    env.process(clock(env, 'slow', 1))
    env.run(until=2.1)

    # r = Resource("id", "value")
    # rr = ResourceRequirement("id", "value")

    # ms = Microservice("app", [], 5000, True)

    gir = GenericIntegerRequirement(IntegerResourceDescriptor(ResourceType.STORAGE, "1000"), "ge")

    ird = IntegerResourceDescriptor(ResourceType.STORAGE, "2500")

    print(gir.rd.res_value)
    print(gir.rd.res_type)

    print(ird.res_value)
    print(ird.res_type)

    ret = gir.is_satisfied_by_resource(ird)

    print(ret)
