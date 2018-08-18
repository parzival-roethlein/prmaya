import random


class Transform(object):
    def __init__(self):
        self._translate = [0.0, 0.0, 0.0]
        self._rotate = [0.0, 0.0, 0.0]
        self._scale = [1.0, 1.0, 1.0]

    @property
    def translate(self):
        return self._translate

    @translate.setter
    def translate(self, value):
        self._translate = list(value)

    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, value):
        self._rotate = list(value)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = list(value)


if __name__ == '__main__':
    xfo1 = Transform()
    xfo1.translate[0] = random.random() * 100
    print('xfo1.translate: {}'.format(xfo1.translate))

    xfo2 = Transform()
    xfo2.translate = xfo1.translate
    xfo2.translate[0] += 5
    print('xfo2.translate: {}'.format(xfo2.translate))
    print('xfo1.translate: {}'.format(xfo1.translate))


