from math import pi
__all__ = ['circle_perimeter', 'circle_area']


def circle_perimeter(r=5):
    c = 2*r*pi
    print(c)


def circle_area(r=5):
    s = pi*r*r
    print(s)
