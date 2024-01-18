

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class A(metaclass=Singleton): pass


class B: pass


if __name__ == '__main__':
    aobjs = [(A()) for _ in range(10)]
    bobjs = [B() for _ in range(10)]

    print([id(a) for a in aobjs])
    print([id(b) for b in bobjs])
