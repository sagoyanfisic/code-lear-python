class Singleton(type):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)
        
    def __call__(cls):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls)
        return cls.__instance

class A:
    __metaclass__ = Singleton


a = A()
b = A()
assert a == b  # True, funciona!  :-)
