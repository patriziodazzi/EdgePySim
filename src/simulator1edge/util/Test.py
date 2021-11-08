from __future__ import annotations


class A(object):
    def __init__(self):
        self.b = B().create()
        self.c = C().create()

    def create(self):
        print("A created")
        return True

    def call(self):
        print(self.b)


class B(object):
    def __init__(self):
        c = C().create()

    def create(self):
        print("B created")
        return True


class C(object):
    def __init__(self):
        print("nothing to create")

    def create(self):
        print("C created")
        return True


if __name__ == '__main__':
    a = A()
    a.call()