from edgepysim.resource.resource import Resource


class ResourceRequirement(Resource):

    def __init__(self, res_type, res_value):
        super().__init__(res_type, res_value)

    def is_satisfied(self, resources: set[Resource]) -> bool:
        pass


class GenericResourceRequirement(ResourceRequirement):

    def __init__(self, res_type, res_value, matching):
        super().__init__(res_type, res_value)
        self.matching = matching

    def is_satisfied(self, resources: set[Resource]) -> bool:

        actual_value = ""

        for r in resources:
            if r.res_type == self.res_type:
                actual_value = r.res_value

        if actual_value == "":
            return False

        if self.matching == "eq":
            return actual_value == self.res_value
        elif self.matching == "gt":
            return actual_value > self.res_value
        elif self.matching == "lt":
            return actual_value < self.res_value
        elif self.matching == "gte":
            return actual_value >= self.res_value
        elif self.matching == "lte":
            return actual_value <= self.res_value

        return False
