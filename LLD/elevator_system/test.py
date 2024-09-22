
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    def __init__(self):
        pass

class OldClass: pass

# class AClass(object): pass

# class BClass(object, metaclass=Singleton): pass


if __name__ == '__main__':
    # print(AClass)
    objs = []
    for _ in range(10):
        mc = OldClass()
        objs.append(mc)

    for ob in objs:
        print(id(ob))

    # print(id(BClass()))
    # print(id(BClass()))


