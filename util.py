#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import gcd


def common_divisor(x1, x2):
    """
    calculate all of the common divisor of x1 and x2

    :param x1: int number
    :param x2: int number
    :return: list of the cd
    """
    _gcd = gcd(x1, x2)
    x1, x2 = calculate_ratio(x1, x2)
    return [(x1*i, x2*i) for i in divisor(_gcd)]


def divisor(x):
    """
    calculate all of the divisor of x

    :param x: int (x > 0)
    :return: list of divisors
    """
    return [i for i in range(1, x+1) if x % i == 0]


def calculate_ratio(x, y):
    """
    calculate the ratio of x and y

    :param x: int
    :param y: int
    :return: (cx, cy) but cx:cy = x:y
    """
    _gcd = gcd(x, y)
    return int(x/_gcd), int(y/_gcd)


if __name__ == '__main__':
    print(calculate_ratio(320, 180))
    print(divisor(gcd(320, 180)))
    ls = common_divisor(320, 180)
    print(ls)
    print(800//(800//16), 800//(800//9))


