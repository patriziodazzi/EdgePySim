from resource.requirement import ResourceRequirement


class Microservice(object):

    def __init__(self, requirements: set[ResourceRequirement]):
        self.requirements = requirements


class Application(object):
    def __init__(self, components: Microservice):
        self.components = components
