import string


class Resource(object):

    def __init__(self, res_type: string, res_value: string):
        self.res_type = res_type
        self.res_value = res_value

    def get_type(self) -> string:
        return self.res_value

    def get_value(self) -> string:
        return self.res_value
