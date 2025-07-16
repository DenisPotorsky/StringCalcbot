from math import pi


def cooperDiamm(general, kern):
    return (general - kern) / 2  # вычисления диаметра меди для одиночной струны


def lengthCoop(kern, cooper, length):
    return (kern + cooper * 2) * pi * length  # вычисления длины меди для одиночной струны


def cooperF(general, kern):
    return ((general - kern) * 0.3334) / 2  # вычисления диаметра меди для первички


def cooperS(general, kern):
    return ((general - kern) * 0.6667) / 2  # вычисления диаметра меди для вторички


def lengthCooperPrim(kern, length, cooperFirst):
    return (kern + cooperFirst * 2) * pi * length - 50  # вычисления длины меди для первички


def lengthCooperSec(kern, length, cooperFirst, cooperSecond):
    return ((kern + (cooperFirst * 2)) + ((cooperSecond * 2))  # вычисления длины меди для вторички
            * pi * length)