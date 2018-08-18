import random


class SetterProperty(object):
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__

    def __set__(self, obj, value):
        return self.func(obj, value)


class Transform(object):
    def __init__(self):
        self.translate = [0.0, 0.0, 0.0]
        self.rotate = [0.0, 0.0, 0.0]
        self.scale = [1.0, 1.0, 1.0]

    @SetterProperty
    def translate(self, value):
        self.__dict__['translate'] = list(value)

    @SetterProperty
    def rotate(self, value):
        self.__dict__['rotate'] = list(value)

    @SetterProperty
    def scale(self, value):
        self.__dict__['scale'] = list(value)


if __name__ == '__main__':
    xfo1 = Transform()
    xfo1.translate[0] = random.random() * 100
    print('xfo1.translate: {}'.format(xfo1.translate))

    xfo2 = Transform()
    xfo2.translate = xfo1.translate
    xfo2.translate[0] += 5
    print('xfo2.translate: {}'.format(xfo2.translate))
    print('xfo1.translate: {}'.format(xfo1.translate))


